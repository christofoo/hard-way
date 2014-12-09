# Example code I found from pymailheaders I"m using for my reading exercise

import constants, sys
from latin1prober import Latin1Prober # windows-1252
from mbcsgroupprober import MBCSGroupProber # multi-byte character sets
from sbcsgroupprober import SBCSGroupProber # single-byte character sets
from escprober import EscCharSetProber # ISO-2122, etc.
import re

MINIMUM_THRESHOLD = 0.20
ePureAscii = 0
eEscAscii = 1
eHighbyte = 2

#class is named UniversalDetector. It doesn't seem to inherit from another class
class UniversalDetector:
    def __init__(self):
        self._highBitDetector = re.compile(r'[\x80-\xFF]')
        self._escDetector = re.compile(r'(\033|~{)')
        self._mEscCharSetProber = None
        self._mCharSetProbers = []
        self.reset()

    def reset(self):
        self.result = {'encoding': None, 'confidence': 0.0}
        self.done = constants.False
        self._mStart = constants.True
        self._mGotData = constants.False
        self._mInputState = ePureAscii
        self._mLastChar = ''
        if self._mEscCharSetProber:
            self._mEscCharSetProber.reset()
        for prober in self._mCharSetProbers:
            prober.reset()

    def feed(self, aBuf):
        if self.done: return

        aLen = len(aBuf)
        if not aLen: return
        
        if not self._mGotData:
            # If the data starts with BOM, we know it is UTF
            if aBuf[:3] == '\xEF\xBB\xBF':
                # EF BB BF  UTF-8 with BOM
                self.result = {'encoding': "UTF-8", 'confidence': 1.0}
            elif aBuf[:4] == '\xFF\xFE\x00\x00':
                # FF FE 00 00  UTF-32, little-endian BOM
                self.result = {'encoding': "UTF-32LE", 'confidence': 1.0}
            elif aBuf[:4] == '\x00\x00\xFE\xFF': 
                # 00 00 FE FF  UTF-32, big-endian BOM
                self.result = {'encoding': "UTF-32BE", 'confidence': 1.0}
            elif aBuf[:4] == '\xFE\xFF\x00\x00':
                # FE FF 00 00  UCS-4, unusual octet order BOM (3412)
                self.result = {'encoding': "X-ISO-10646-UCS-4-3412", 'confidence': 1.0}
            elif aBuf[:4] == '\x00\x00\xFF\xFE':
                # 00 00 FF FE  UCS-4, unusual octet order BOM (2143)
                self.result = {'encoding': "X-ISO-10646-UCS-4-2143", 'confidence': 1.0}
            elif aBuf[:4] == '\xFF\xFE':
                # FF FE  UTF-16, little endian BOM
                self.result = {'encoding': "UTF-16LE", 'confidence': 1.0}
            elif aBuf[:2] == '\xFE\xFF':
                # FE FF  UTF-16, big endian BOM
                self.result = {'encoding': "UTF-16BE", 'confidence': 1.0}

        self._mGotData = constants.True
        if self.result['encoding'] and (self.result['confidence'] > 0.0):
            self.done = constants.True
            return

        if self._mInputState == ePureAscii:
            if self._highBitDetector.search(aBuf):
                self._mInputState = eHighbyte
            elif (self._mInputState == ePureAscii) and self._escDetector.search(self._mLastChar + aBuf):
                self._mInputState = eEscAscii

        self._mLastChar = aBuf[-1]

        if self._mInputState == eEscAscii:
            if not self._mEscCharSetProber:
                self._mEscCharSetProber = EscCharSetProber()
            if self._mEscCharSetProber.feed(aBuf) == constants.eFoundIt:
                self.result = {'encoding': self._mEscCharSetProber.get_charset_name(),
                               'confidence': self._mEscCharSetProber.get_confidence()}
                self.done = constants.True
        elif self._mInputState == eHighbyte:
            if not self._mCharSetProbers:
                self._mCharSetProbers = [MBCSGroupProber(), SBCSGroupProber(), Latin1Prober()]
            for prober in self._mCharSetProbers:
                if prober.feed(aBuf) == constants.eFoundIt:
                    self.result = {'encoding': prober.get_charset_name(),
                                   'confidence': prober.get_confidence()}
                    self.done = constants.True
                    break

    def close(self):
        if self.done: return
        if not self._mGotData:
            if constants._debug:
                sys.stderr.write('no data received!\n')
            return
        self.done = constants.True
        
        if self._mInputState == ePureAscii:
            self.result = {'encoding': 'ascii', 'confidence': 1.0}
            return self.result

        if self._mInputState == eHighbyte:
            proberConfidence = None
            maxProberConfidence = 0.0
            maxProber = None
            for prober in self._mCharSetProbers:
                if not prober: continue
                proberConfidence = prober.get_confidence()
                if proberConfidence > maxProberConfidence:
                    maxProberConfidence = proberConfidence
                    maxProber = prober
            if maxProber and (maxProberConfidence > MINIMUM_THRESHOLD):
                self.result = {'encoding': maxProber.get_charset_name(),
                               'confidence': maxProber.get_confidence()}
                return self.result

        if constants._debug:
            sys.stderr.write('no probers hit minimum threshhold\n')
            for prober in self._mCharSetProbers[0].mProbers:
                if not prober: continue
                sys.stderr.write('%s confidence = %s\n' % \
                                 (prober.get_charset_name(), \
                                  prober.get_confidence()))




########## From another file:


# called utf8prober.py from pymailheaders

import constants, sys
from constants import eStart, eError, eItsMe
from charsetprober import CharSetProber
from codingstatemachine import CodingStateMachine
from mbcssm import UTF8SMModel

ONE_CHAR_PROB = 0.5
#class is called UTF8Prober and it inherits from CharSetProber
class UTF8Prober(CharSetProber):
    def __init__(self):
        CharSetProber.__init__(self)
        self._mCodingSM = CodingStateMachine(UTF8SMModel)
        self.reset()

    def reset(self):
        CharSetProber.reset(self)
        self._mCodingSM.reset()
        self._mNumOfMBChar = 0

    def get_charset_name(self):
        return "utf-8"

    def feed(self, aBuf):
        for c in aBuf:
            codingState = self._mCodingSM.next_state(c)
            if codingState == eError:
                self._mState = constants.eNotMe
                break
            elif codingState == eItsMe:
                self._mState = constants.eFoundIt
                break
            elif codingState == eStart:
                if self._mCodingSM.get_current_charlen() >= 2:
                    self._mNumOfMBChar += 1

        if self.get_state() == constants.eDetecting:
            if self.get_confidence() > constants.SHORTCUT_THRESHOLD:
                self._mState = constants.eFoundIt

        return self.get_state()

    def get_confidence(self):
        unlike = 0.99
        if self._mNumOfMBChar < 6:
            for i in range(0, self._mNumOfMBChar):
                unlike = unlike * ONE_CHAR_PROB
            return 1.0 - unlike
        else:
            return unlike

############# I'm gonna also put pymailheaders.py on here:


from threading import Thread
from threading import Lock
from threading import Event
from optparse import OptionParser
from datetime import datetime
import sys
import re
import os
import os.path
import locale
import gettext
import logging

# switch to the directory where this file resides in, so that it can find the
# glade file
app_name = 'pymailheaders'
cwd = os.getcwd()
basedir = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(os.path.join(basedir, '%s.py' % app_name.lower())):
    if os.path.exists(os.path.join(cwd, '%s.py' % app_name.lower())):
        basedir = cwd
sys.path.insert(0, basedir)
os.chdir(basedir)

# set to default locale
locale.setlocale(locale.LC_ALL, '')

# load translation file
gettext.bindtextdomain(app_name, 'po')
gettext.textdomain(app_name)
import __builtin__
__builtin__._ = lambda x: x
try:
    locales = locale.getdefaultlocale()
    if locales[0]:
        trans = gettext.translation(app_name, 'po', [locales[0]])
        if trans:
            __builtin__._ = trans.ugettext
except IOError:
    pass

import signal
import gui
import imapprl
import popprl
import feedprl
import config
import constants
from exception import *

# global varibals
checker = None
mail_thrs = {}
gui_thr = None
conf = None

lock = Lock()
messages = ({}, {})

JOIN_TIMEOUT = 1.0

class mail_thread(Thread):
    """This class creates the thread for fetching messages.

    @note: Private member variables:
        __timer
        __name
        __interval
        __mail_obj
    """

    def __init__(self, name, t, server, uname, password, ssl, h, interval,
                 mbox = 'INBOX'):
        """Override constructor

        @type name: string
        @param name: account name
        @type t: string
        @param t: server type
        @type server: string
        @param server: mail server address
        @type uname: string
        @param uname: username
        @type password: string
        @param password: password
        @type ssl: bool
        @param ssl: if this is a secure connection
        @type h: int
        @param h: number of messages displayable in the window
        @type interval: int
        @param interval: time interval between updates
        @type mbox: string
        @param mbox: mailbox.
            I{Default = 'INBOX'}
        """

        global mail_thrs

        Thread.__init__(self, group = None, target = None,
                        name = 'mail-thread-%s-%d' % (t, len(mail_thrs)),
                        args = (), kwargs = {})

        self.__name = name
        self.__interval = float(interval)
        self.__logger = logging.getLogger(self.getName())
        if not globals().has_key('%sprl' % t):
            self.__logger.error(_('pymailheaders: unknown server type %s'), t)
            sys.exit(1)
        self.__mail_obj = getattr(globals()['%sprl' % t], t)(server,
                                                             uname,
                                                             password,
                                                             ssl,
                                                             h,
                                                             mbox)
        self.__timer = Event()

    def quit(self):
        """Terminates the mail thread.
        """

        self.__timer.set()

    def fetch(self):
        """Check and get mails

        This will set the global variables messages. messages will be in the form

        ({name: [(datetime, sender, subject), ...], ...},  <--- unread mails
         {name: [(datetime, sender, subject), ...], ...})  <--- read mails

        This allows each account to clear its own section when updating.
        """

        global messages
        global lock

        try:
            self.__logger.debug('Get mail')

            res = self.__mail_obj.get_mail()
            lock.acquire()
            messages[0][self.__name] = res[0]
            messages[1][self.__name] = res[1]
            lock.release()
        except TryAgain:
            self.__logger.info('Network not available')

            lock.acquire()
            messages[0].clear()
            messages[1].clear()
            messages[0][self.__name] = [(datetime.now(), _('Error'),
                                         _('Network not available'))]
            lock.release()
        except Error, strerr:
            self.__logger.error(str(strerr))

            lock.acquire()
            messages[0].clear()
            messages[1].clear()
            messages[0][self.__name] = [(datetime.now(), _('Error'),
                                         str(strerr))]
            lock.release()

    def refresh(self):
        """Fetches mail and updates the GUI.
        """

        self.fetch()

        self.__logger.debug('Update gui when it is idle')

        gui.gobject.idle_add(update_gui)

    def run(self):
        """Connect to the server and fetch for the first time
        """

        global checker

        while not self.__timer.isSet():
            checker.add(self)
            self.__logger.debug('Starting timer')
            self.__timer.wait(self.__interval)
            self.__logger.debug('Timer set')
        self.__logger.debug('Terminating...')

class mail_checker(Thread):
    """This class checks for mails in each account.

    @note: Private member variables:
        __unchecked
        __quit
        __flag
        __lock
    """

    def __init__(self):
        Thread.__init__(self, group = None, target = None,
                        name = 'mail-checker', args = (), kwargs = {})
        self.setDaemon(True)

        self.__unchecked = []
        self.__quit = False
        self.__flag = Event()
        self.__lock = Lock()
        self.__logger = logging.getLogger(self.getName())

    def __check(self, mail_thread):
        """Call the mail checking method on the mail thread.

        @type mail_thread: mail_thread
        @param mail_thread: the mail thread to check
        """

        mail_thread.refresh()

    def quit(self):
        """Terminates the checker.
        """

        self.__quit = True
        self.__flag.set()

    def add(self, mail_thread):
        """Add the mail thread to the queue waiting to be checked.

        @type mail_thread: mail_thread
        @param mail_thread: the mail thread to check
        """

        if not mail_thread:
            return

        self.__lock.acquire()
        if mail_thread not in self.__unchecked:
            self.__unchecked.append(mail_thread)
        self.__logger.debug('%s added to the checking queue (%d)' %
                            (mail_thread.getName(), len(self.__unchecked)))
        self.__lock.release()

        self.__flag.set()

    def run(self):
        """Starts the loop of checking for mails.
        """

        while not self.__quit:
            self.__flag.clear()

            self.__lock.acquire()
            while self.__unchecked:
                self.__check(self.__unchecked.pop(0))
            self.__lock.release()

            self.__flag.wait()

# update GUI
def update_gui():
    """The variable passed to the GUI thread is in the following form

    ([(name, datetime, sender, subject), ...],  <--- unread mails
     [(name, datetime, sender, subject), ...])  <--- read mails

    sorted in reverse chronological order.
    """

    global lock
    global messages
    global gui_thr

    msgs = ([], [])

    logging.debug('Update gui')

    lock.acquire()
    for k, v in messages[0].iteritems():
        for j in v:
            msgs[0].append((k, j[0], j[1], j[2]))
    for k, v in messages[1].iteritems():
        for j in v:
            msgs[1].append((k, j[0], j[1], j[2]))
    lock.release()

    cmp_func = lambda x, y: cmp(x[1], y[1])
    msgs[0].sort(cmp_func, reverse = True)
    msgs[1].sort(cmp_func, reverse = True)
    gui_thr.display(msgs)

def on_refresh_activate():
    global mail_thrs
    global checker

    for acct in  mail_thrs.itervalues():
        checker.add(acct)

def on_account_changed(opts):
    global conf
    global mail_thrs
    global lock
    global messages

    for k, v in opts.iteritems():
        delete_mail_thr(k)

        # if the account name has changed
        if 'name' in v:
            lock.acquire()
            if k in messages[0]:
                del messages[0][k]
            if k in messages[1]:
                del messages[1][k]
            lock.release()
            conf.remove_account(k)
            k = v['name']

        new_mail_thr(k, v)
        if k in mail_thrs and not mail_thrs[k].isAlive():
            mail_thrs[k].start()

def on_account_removed(name):
    global conf
    global lock
    global messages

    lock.acquire()
    if name in messages[0]:
        del messages[0][name]
    if name in messages[1]:
        del messages[1][name]
    lock.release()

    delete_mail_thr(name)
    conf.remove_account(name)

def on_config_save(opts):
    global conf

    if type(opts) != dict:
        return

    # write settings to config file
    for k, v in opts.iteritems():
        if k == 'accounts':
            for name, opt in v.iteritems():
                for i, j in opt.iteritems():
                    conf.set(i, j, name)
        else:
            conf.set(k, v)
    conf.write()

def on_exit(signum = None, frame = None):
    logging.debug('Quit')

    gui.gtk.quit()

def new_mail_thr(name, opts):
    global mail_thrs
    global gui_thr
    global conf

    if type(opts) != dict or name in mail_thrs:
        return

    logging.debug('Create new mail thread')

    acct = conf.make_empty_acct()
    acct.update(opts)

    if not acct['type'] or not acct['server'] or \
            (acct['auth'] and (not acct['username'] or not acct['password'])):
        gui_thr.show_settings(None)
        return

    h = gui_thr.get_max_messages()
    mail_thrs[name] = mail_thread(name, acct['type'], acct['server'],
                                  acct['username'], acct['password'],
                                  acct['encrypted'], h, acct['interval'])

def new_mail_thrs(opts):
    global mail_thrs
    global gui_thr

    if type(opts) != dict or mail_thrs:
        return

    for k, v in opts.iteritems():
        new_mail_thr(k, v)

def delete_mail_thr(name):
    global mail_thrs

    if not mail_thrs or name not in mail_thrs:
        return

    logging.debug('Delete mail thread %s' % name)

    mail_thrs[name].quit()
    mail_thrs[name].join(JOIN_TIMEOUT)
    del mail_thrs[name]

def delete_mail_thrs():
    # get a list of all the mail threads first, otherwise the dictionary size
    # will change in the middle of this process
    keys = mail_thrs.keys()

    # stop all mail threads
    for k in keys:
        delete_mail_thr(k)

def is_posix():
    if sys.platform == 'win32':
        return False
    elif sys.platform == 'win64':
        return False
    else:
        return True

def main():
    """Main function
    """

    global lock
    global conf
    global gui_thr
    global mail_thrs
    global checker
    global messages

    # parse command-line arguments
    usage = 'usage: %prog [options]... args...'
    parser = OptionParser(usage)
    parser.add_option('-c', '--config-file', dest = 'config',
                      help = 'configuration file path')
    parser.add_option('-w', '--width', dest = 'width', type = 'int',
                      help = 'width of the window')
    parser.add_option('-g', '--height', dest = 'height', type = 'int',
                      help = 'height of the window')
    parser.add_option('--bg', dest = 'background', help = 'backgound color')
    parser.add_option('--fg', dest = 'foreground',
                      help = 'foreground color')
    parser.add_option('--fgn', dest = 'foreground new',
                      help = 'foreground color for new messages')
    parser.add_option('-l', '--log', dest = 'log',
                      help = 'Log file')
    parser.add_option('--level', dest = 'level',
                      help = 'Log level: critial, error, warning, info, debug')
    (options, args) = parser.parse_args()

    if options.config:
        exp_path = os.path.expanduser(options.config)
        config_file = os.path.isabs(exp_path) and exp_path or \
            os.path.join(cwd, exp_path)
    else:
        # default config file location
        if is_posix():
            config_file = os.path.expanduser('~/.pymailheadersrc')
        else:
            config_file = 'config.ini'

    try:
        # read in config file if there is any
        conf = config.config(config_file)
    except:
        sys.exit(1)

    # get all configurations
    #
    # command line arguments have higher priorities, so they can overwrite
    # config file options
    opts = conf.get_all()

    # this is way too ugly, it's not a proper use of optparse, but had to
    # use this hack to get arround.
    options = options.__dict__.copy()
    del options['config']

    # don't use opts.update() because that will write all None values
    for k in options.iterkeys():
        if not opts.has_key(k) or options[k]:
            opts[k] = options[k]

    # Logging information
    if 'log' in opts:
        TARGET = opts['log']
        del opts['log']
    else:
        TARGET = None
    LEVEL_LIST = {'critical': logging.CRITICAL,
                  'error': logging.ERROR,
                  'warning': logging.WARNING,
                  'info': logging.INFO,
                  'debug': logging.DEBUG}
    if 'level' in opts and opts['level'] in LEVEL_LIST:
        LEVEL = LEVEL_LIST[opts['level']]
    else:
        LEVEL = LEVEL_LIST['error']
    if 'level' in opts:
        del opts['level']
    FORMAT = '%(asctime)s [(%(threadName)-13s) %(name)-11s:%(lineno)-4d]' + \
        ' %(levelname)-5s: %(message)s'
    logging.basicConfig(level = LEVEL,
                        format = FORMAT,
                        datefmt = '%H:%M:%S',
                        filename = TARGET)

    # setup signal handler so that settings will be saved even if the
    # process is killed
    signal.signal(signal.SIGTERM, on_exit)

    # create threads
    gui_thr = gui.gui(opts)

    # set up signal handlers
    handlers = {'on_refresh_activate': on_refresh_activate,
                'on_config_save': on_config_save,
                'on_account_changed': on_account_changed,
                'on_account_removed': on_account_removed}
    gui_thr.signal_autoconnect(handlers)

    new_mail_thrs(opts['accounts'])
    checker = mail_checker()

    try:
        # start all threads
        checker.start()

        for mail_thr in mail_thrs.itervalues():
            if not mail_thr.isAlive():
                mail_thr.start()

        gui.gtk.gdk.threads_enter()
        gui.gtk.main()
        gui.gtk.gdk.threads_leave()
    except KeyboardInterrupt:
        pass

    checker.quit()

    delete_mail_thrs()

# rock n' roll
if __name__ == '__main__':
    main()

# Exercises:

# 1. For each class give its name and what other classes it inherits from.
# 2. Under that, list every function it has and the parameters they take.
# 3. List all of the attributes it uses on its self.
# 4. For each attribute, give the class this attribute is.


### List
# class UniversalDetector:
# def __init__(self):
# def reset(self):
# def feed(self, aBuf):
# def close(self):

# class UTF8Prober(CharSetProber):
# def __init__(self):
# def reset(self):
# def get_charset_name(self):
# def feed(self, aBuf):
# def get_confidence(self):

#I'm skipping these first 2 classes for questions 3 and 4 just so I can read better...

##############################################################################################


# class mail_thread(Thread):
# def __init__(self, name, t, server, uname, password, ssl, h, interval,
#                  mbox = 'INBOX'):
# self.__name = name

# no clue what class __name is. I guess it's mail_thread

# self.__interval = float(interval)

# is it's class just mail_thread?

# self.__logger = logging.getLogger(self.getName())

#its class is mail_thread I guess

# self.__logger.error(_('pymailheaders: unknown server type %s'), t)
#             sys.exit(1)

## mail thread


# self.__mail_obj = getattr(globals()['%sprl' % t], t)(server,
#                                                              uname,
#                                                              password,
#                                                              ssl,
#                                                              h,
#                                                              mbox)

# mail thread 

#         self.__timer = Event()


#mail thread 


# 

# def quit(self):

# self.__timer.set()

#mail thread I guess

# def fetch(self):

# self.__logger.debug('Get mail')

# mail thread...



# self.__logger.info('Network not available')

#mail thread...


#  self.__logger.error(str(strerr))

# mail thread...

# def refresh(self):

# self.fetch()

#mail thread....


# self.__logger.debug('Update gui when it is idle')

#mail_thread

# def run(self):

# self.__logger.debug('Starting timer')

#yeah these are all mail thread.. i dont get it

#             self.__timer.wait(self.__interval)
#             self.__logger.debug('Timer set')
#         self.__logger.debug('Terminating...')









# class mail_checker(Thread):

# def __init__(self):

# self.setDaemon(True)

#         self.__unchecked = []
#         self.__quit = False
#         self.__flag = Event()
#         self.__lock = Lock()
#         self.__logger = logging.getLogger(self.getName())

# def __check(self, mail_thread):



# def quit(self):

 # self.__quit = True
 #        self.__flag.set()

# def add(self, mail_thread):

  # self.__lock.acquire()
  #       if mail_thread not in self.__unchecked:
  #           self.__unchecked.append(mail_thread)
  #       self.__logger.debug('%s added to the checking queue (%d)' %
  #                           (mail_thread.getName(), len(self.__unchecked)))
  #       self.__lock.release()

  #       self.__flag.set()

# def run(self):

 # while not self.__quit:
 #            self.__flag.clear()

 #            self.__lock.acquire()
 #            while self.__unchecked:
 #                self.__check(self.__unchecked.pop(0))
 #            self.__lock.release()

 #            self.__flag.wait()

# def update_gui():



# def on_refresh_activate():



# def on_account_changed(opts):



# def on_account_removed(name):



# def on_config_save(opts):



# def on_exit(signum = None, frame = None):



# def new_mail_thr(name, opts):



# def new_mail_thrs(opts):



# def delete_mail_thr(name):



# def delete_mail_thrs():



# def is_posix():



# def main():