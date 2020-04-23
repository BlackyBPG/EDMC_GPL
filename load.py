"""
The "German Pilot Lounge" Plugin
+ extendet with functionality to show all factions
"""
import l10n
import functools
from config import config
import myNotebook as nb

_ = functools.partial(l10n.Translations.translate, context=__file__)

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import sys
import time
from l10n import Locale

this = sys.modules[__name__]  # For holding module globals
this.showgpl = tk.IntVar(value=1)
this.showrep = tk.IntVar(value=1)
this.showpil = tk.IntVar(value=0)

APP_VERSION = "20.04.20_b1944"

COLOR_R_RED = [64,64,64,64,64,64,64,64,64,64,65,66,67,68,70,71,72,73,74,76,77,78,79,80,82,83,84,85,86,88,89,90,91,92,94,95,96,97,98,100,101,102,103,104,106,107,108,109,110,112,113,114,115,116,118,119,120,121,122,124,125,126,127,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,130,132,134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,164,166,168,170,173,176,179,182,185,188,191,194,197,200,203,206,209,212,215,218,221,224,227,230,233,236,239,242,245,248,251,254,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255]
COLOR_R_GREEN = [255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,251,247,243,239,235,231,227,223,219,215,211,207,203,199,195,191,187,183,179,175,171,175,179,183,187,191,195,199,203,207,211,215,219,223,227,231,235,239,243,247,251,255,252,249,246,243,240,237,234,231,228,225,222,219,216,213,210,207,204,201,198,195,192,189,186,183,180,177,174,171,168,165,162,159,156,153,150,147,144,141,138,135,132,129,126,123,120,117,114,111,108,105,102,99,96,93,90,87,84,81,78,75,72,69,66]
COLOR_R_BLUE = [64,64,64,64,64,64,64,64,64,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,164,166,168,170,172,174,176,179,181,184,186,189,191,194,196,199,201,204,206,209,211,214,216,219,221,224,226,229,231,234,236,239,241,244,246,249,251,255,251,247,243,239,235,231,227,223,219,215,211,207,203,199,195,191,187,183,179,175,171,165,159,154,148,142,137,131,125,120,114,108,103,97,91,86,80,74,69,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64]

COLOR_I_RED = [64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,66,69,71,74,77,79,82,85,87,90,93,95,98,101,103,106,109,111,114,117,119,122,125,127,130,133,135,138,141,143,146,149,151,154,157,159,162,165,167,170,173,175,178,181,183,186,189,191,194,197,199,202,205,207,210,213,215,218,221,223,226,229,231,234,237,239,242,245,247,250,253,255,255,255,255,255]
COLOR_I_GREEN = [255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,253,250,248,245,243,240,238,235,233,230,228,225,223,220,218,215,213,210,208,205,203,200,198,195,193,190,188,185,183,180,178,175,173,170,168,165,163,160,158,155,153,150,148,145,143,140,138,135,133,130,128,125,123,120,118,115,113,110,108,105,103,100,98,95,93,90,88,85,83,80,78,75,73,70,68]
COLOR_I_BLUE = [64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64]

COLOR_NORM = ("#000000", "#80FFFF", "#0018C9", "#FF8000")

MAX_FACTIONS = 14
DEFAULT_SHOWGPL = 1
DEFAULT_SHOWREP = 1
DEFAULT_SHOWPIL = 0
DEFAULT_SHOWOTH = 1
DEFAULT_SHOWCOL = 1
NAME_PIL = "Pilots' Federation Local Branch"
NAME_GPL = "German Pilot Lounge"
NAME_GPL_SHORT = "GPL"
NAME_REPUTATION = "Reputation"

CFG_GPL_SHOW = "gpl_showgpl"
CFG_GPL_COL = "gpl_showcol"
CFG_GPL_PIL = "gpl_showpil"
CFG_GPL_OTH = "gpl_showoth"
CFG_GPL_REP = "gpl_showrep"
CFG_DESIGN = "gpl_design"

class Gpl(object):
    """
    The main class for the gpl plugin
    """
    widget_Name = []
    widget_State = []
    widget_Desc = []
    widget_Perc = []
    reputation = 0
    influence = 0
    oldlen = 0
    systemfaction = []
    systemfactioninflu = []
    systemfactionstate = []
    systemfactionmode = []
    showgpl = 1
    showrep = 1
    showpil = 0
    showoth = 1
    showcol = 1
    appdesign = 0
    initializeMe = True

    def load(self):
        if config.get(CFG_DESIGN):
            self.appdesign = int(config.get(CFG_DESIGN))
        else:
           self.appdesign = 0

        if config.get(CFG_GPL_SHOW):
            self.showgpl = int(config.get(CFG_GPL_SHOW))
        else:
           self.showgpl = DEFAULT_SHOWGPL

        if config.get(CFG_GPL_REP):
            self.showrep = int(config.get(CFG_GPL_REP))
        else:
            self.showrep = DEFAULT_SHOWREP

        if config.get(CFG_GPL_PIL):
            self.showpil = int(config.get(CFG_GPL_PIL))
        else:
            self.showpil = DEFAULT_SHOWPIL

        if config.get(CFG_GPL_OTH):
            self.showoth = int(config.get(CFG_GPL_OTH))
        else:
            self.showoth = DEFAULT_SHOWOTH

        if config.get(CFG_GPL_COL):
            self.showcol = int(config.get(CFG_GPL_COL))
        else:
            self.showcol = DEFAULT_SHOWCOL

        self.reputation = 0
        self.influence = 0
        self.oldlen = 0
        self.systemfaction = []
        self.systemfactioninflu = []
        self.systemfactionmode = []
        self.initializeMe = True

    def data_systemfaction(self, index, sysfaction, influence, state, mode):
        if mode == "RESET":
            self.systemfaction = []
            self.systemfactioninflu = []
            self.systemfactionstate = []
            self.systemfactionmode = []
        else:
            if len(self.systemfaction) == 0:
                self.systemfaction.append(sysfaction)
                self.systemfactioninflu.append(influence)
                self.systemfactionstate.append(state)
                self.systemfactionmode.append(mode)
            else:
                x = 0
                y = len(self.systemfaction)
                insin = y
                if mode == NAME_GPL_SHORT:
                    insin = 0
                elif mode == NAME_REPUTATION:
                    insin = 1
                else:
                    while x < y:
                        if insin > x and self.systemfactioninflu[x] <= influence and self.systemfactionmode[x] != NAME_GPL_SHORT and self.systemfactionmode[x] != NAME_REPUTATION:
                            insin = x

                        x = x + 1

                self.systemfaction.insert(insin, sysfaction)
                self.systemfactioninflu.insert(insin, influence)
                self.systemfactionstate.insert(insin, state)
                self.systemfactionmode.insert(insin, mode)

        self.update_window()

    def update_window(self):
        self.update_systemfactions()

    def update_systemfactions(self):
        x = 0
        xd = 0
        if len(self.systemfaction) > 0:
            self.frame.grid()
            self.oldlen = len(self.systemfaction)
            while x < len(self.systemfaction):
                if self.showpil == 0 and self.systemfaction[x] == NAME_PIL:
                    xd = xd + 1
                elif self.showgpl == 0 and self.systemfactionmode[x] == NAME_GPL_SHORT:
                    xd = xd + 1
                elif self.showrep == 0 and self.systemfactionmode[x] == NAME_REPUTATION:
                    xd = xd + 1
                elif self.showoth == 0 and not ((self.systemfactionmode[x] == NAME_REPUTATION and self.showrep == 1) or (self.systemfactionmode[x] == NAME_GPL_SHORT and self.showgpl == 1)):
                    xd = xd + 1
                else:
                    self.widget_Name[x-xd].grid(row=x-xd, column=0, sticky=tk.W)
                    self.widget_State[x-xd].grid(row=x-xd, column=1, sticky=tk.E+tk.W, padx=10)
                    if self.systemfactionmode[x] == NAME_REPUTATION or self.systemfactionmode[x] == NAME_GPL_SHORT:
                        self.widget_Name[x-xd]["foreground"] = COLOR_NORM[self.appdesign+2]
                    else:
                        self.widget_Name[x-xd]["foreground"] = COLOR_NORM[self.appdesign]

                    if self.systemfactionmode[x] == "SYS":
                        self.widget_Name[x-xd].after(0, self.widget_Name[x-xd].config, {"text": "! " + self.systemfaction[x]})
                    else:
                        self.widget_Name[x-xd].after(0, self.widget_Name[x-xd].config, {"text": self.systemfaction[x]})

                    self.widget_State[x-xd].after(0, self.widget_State[x-xd].config, {"text": self.systemfactionstate[x]})

                    msg = "{}".format(Locale.stringFromNumber(self.systemfactioninflu[x], 3))
                    self.widget_Desc[x-xd].grid(row=x-xd, column=2, sticky=tk.E)
                    if self.showcol == 1:
                        red = COLOR_I_RED[int(100 - self.systemfactioninflu[x])]
                        green = COLOR_I_GREEN[int(100 - self.systemfactioninflu[x])]
                        blue = COLOR_I_BLUE[int(100 - self.systemfactioninflu[x])]
                        if self.systemfactionmode[x] == NAME_REPUTATION:
                            red = COLOR_R_RED[int(100 - self.reputation)]
                            green = COLOR_R_GREEN[int(100 - self.reputation)]
                            blue = COLOR_R_BLUE[int(100 - self.reputation)]

                        themeval = 64 * (1 - self.appdesign)
                        hexrgb = "#%02x%02x%02x" % (red - themeval, green - themeval, blue - themeval)
                        self.widget_Desc[x-xd]["foreground"] = hexrgb

                    self.widget_Desc[x-xd].after(0, self.widget_Desc[x-xd].config, {"text": msg})

                    self.widget_Perc[x-xd].grid(row=x-xd, column=3, sticky=tk.W)

                x = x + 1

            x = x - xd
            y = x
            while x < MAX_FACTIONS:
                self.widget_Name[x].grid_forget()
                self.widget_State[x].grid_forget()
                self.widget_Desc[x].grid_forget()
                self.widget_Perc[x].grid_forget()
                x = x + 1

            if y == 0:
                self.frame.grid_remove()

        else:
            while x < MAX_FACTIONS:
                self.widget_Name[x].grid_forget()
                self.widget_State[x].grid_forget()
                self.widget_Desc[x].grid_forget()
                self.widget_Perc[x].grid_forget()
                x = x + 1

            if self.oldlen > 0:
                self.frame.grid_remove()
                self.oldlen = 0



def plugin_prefs(parent, cmdr, is_beta):
    if config.get(CFG_GPL_SHOW) != None:
        this.showgpl = tk.IntVar(value=config.get(CFG_GPL_SHOW))
    else:
        this.showgpl = tk.IntVar(value=DEFAULT_SHOWGPL)

    if config.get(CFG_GPL_REP) != None:
        this.showrep = tk.IntVar(value=config.get(CFG_GPL_REP))
    else:
        this.showrep = tk.IntVar(value=DEFAULT_SHOWREP)

    if config.get(CFG_GPL_PIL) != None:
        this.showpil = tk.IntVar(value=config.get(CFG_GPL_PIL))
    else:
        this.showpil = tk.IntVar(value=DEFAULT_SHOWPIL)

    if config.get(CFG_GPL_OTH) != None:
        this.showoth = tk.IntVar(value=config.get(CFG_GPL_OTH))
    else:
        this.showoth = tk.IntVar(value=DEFAULT_SHOWOTH)

    if config.get(CFG_GPL_COL) != None:
        this.showcol = tk.IntVar(value=config.get(CFG_GPL_COL))
    else:
        this.showcol = tk.IntVar(value=DEFAULT_SHOWCOL)

    if config.get(CFG_DESIGN) != None:
        this.appdesign = tk.IntVar(value=config.get(CFG_DESIGN))
    else:
        this.appdesign = tk.IntVar(value=0)


    frame = nb.Frame(parent)
    nb.Label(frame, text="GPL-EDMC Version: {INSTALLED}\n".format(INSTALLED=APP_VERSION)).grid(padx=10, sticky=tk.W)
    nb.Checkbutton(frame, text=_("1. Show other System Factions").encode('utf-8'), variable=this.showoth, onvalue = 1, offvalue = 0).grid(padx=10, pady = 3, sticky=tk.W)
    nb.Checkbutton(frame, text=_("1.A. Show 'Pilots' Federation Local Branch'-Faction in Factionlist (only if Option 1 active)").encode('utf-8'), variable=this.showpil, onvalue = 1, offvalue = 0).grid(padx=10, pady = 3, sticky=tk.W)
    nb.Checkbutton(frame, text=_("2. Show Extra influence for GPL-Faction").encode('utf-8'), variable=this.showgpl, onvalue = 1, offvalue = 0).grid(padx=10, pady = 3, sticky=tk.W)
    nb.Checkbutton(frame, text=_("3. Show own Reputation for GPL").encode('utf-8'), variable=this.showrep, onvalue = 1, offvalue = 0).grid(padx=10, pady = 3, sticky=tk.W)
    nb.Checkbutton(frame, text=_("4. Show colorized percentage values").encode('utf-8'), variable=this.showcol, onvalue = 1, offvalue = 0).grid(padx=10, pady = 3, sticky=tk.W)
    nb.Checkbutton(frame, text=_("Dark Theme").encode('utf-8'), variable=this.appdesign, onvalue = 1, offvalue = 0).grid(padx=10, pady = 20, sticky=tk.W)
    return frame


def prefs_changed(cmdr, is_beta):
    gpl = this.gpl
    gpl.showgpl = int(this.showgpl.get())
    gpl.showrep = int(this.showrep.get())
    gpl.showpil = int(this.showpil.get())
    gpl.showoth = int(this.showoth.get())
    gpl.showcol = int(this.showcol.get())
    gpl.appdesign = int(this.appdesign.get())
    config.set(CFG_GPL_SHOW, str(gpl.showgpl))
    config.set(CFG_GPL_REP, str(gpl.showrep))
    config.set(CFG_GPL_PIL, str(gpl.showpil))
    config.set(CFG_GPL_OTH, str(gpl.showoth))
    config.set(CFG_GPL_COL, str(gpl.showcol))
    config.set(CFG_DESIGN, str(gpl.appdesign))
    gpl.update_window()


def plugin_start3(plugin_dir):
    gpl = Gpl()
    gpl.load()
    this.gpl = gpl

def plugin_start():
    gpl = Gpl()
    gpl.load()
    this.gpl = gpl

def plugin_app(parent):
    gpl = this.gpl

    frame = tk.Frame(parent)

    i = 0
    while i < MAX_FACTIONS:
        objectname = tk.Label(frame, text="", justify=tk.LEFT, foreground="#80FFFF")
        objectname.grid(row=i, column=0, sticky=tk.W)
        gpl.widget_Name.append(objectname)
        objectdesc = tk.Label(frame, text="", justify=tk.RIGHT)
        objectdesc.grid(row=i, column=1, sticky=tk.W+tk.E, padx=10)
        gpl.widget_State.append(objectdesc)
        objectdesc = tk.Label(frame, text="", justify=tk.RIGHT)
        objectdesc.grid(row=i, column=2, sticky=tk.E)
        gpl.widget_Desc.append(objectdesc)
        objectperc = tk.Label(frame, text="%", justify=tk.LEFT)
        objectperc.grid(row=i, column=3, sticky=tk.W)
        gpl.widget_Perc.append(objectperc)
        i = i + 1
    
    
    frame.columnconfigure(0, weight=2)
    frame.columnconfigure(1, weight=2)
    frame.columnconfigure(2, weight=3)
    frame.columnconfigure(3, weight=1)

    this.spacer = tk.Frame(frame)
    gpl.frame = frame
    gpl.update_window()
    return frame


def dashboard_entry(cmdr, is_beta, entry):
    this.gpl.update_window()


def journal_entry(cmdr, is_beta, system, station, entry, state):
    """
    Process a journal event
    :param cmdr:
    :param system:
    :param station:
    :param entry:
    :param state:
    :return:
    """
    if "event" in entry:
        if this.gpl.initializeMe == True:
            this.gpl.initializeMe = False

        if "FSDJump" in entry["event"] or "Location" in entry["event"]:
            this.gpl.data_systemfaction(0,"","","","RESET")
            fact = "[]"
            msginflu = 0
            msgrepu = 0
            sysfac = None
            if entry["SystemFaction"]:
                sysfac = dict(entry["SystemFaction"])

            if "Factions" in entry:
                fact = list(entry["Factions"])
                for i in range(len(fact)):
                    faction = dict(fact[i])
                    if faction["Name"] == NAME_GPL:
                        msginflu = faction["Influence"] * 100
                        msgrepu = faction["MyReputation"]
                        this.gpl.data_systemfaction(i,_("GPL Influence:").encode('utf-8'),msginflu,"",NAME_GPL_SHORT)
                        this.gpl.data_systemfaction(i,_("Own GPL-Reputation:").encode('utf-8'),msgrepu,"",NAME_REPUTATION)

                    mode = "None"
                    if sysfac != None:
                        if sysfac["Name"] == faction["Name"]:
                            mode = "SYS"
                    if faction["FactionState"] == "None":
                        this.gpl.data_systemfaction(i,faction["Name"],faction["Influence"] * 100,"",mode)
                    else:
                        factionstatelng = _(faction["FactionState"]).encode('utf-8')
                        this.gpl.data_systemfaction(i,faction["Name"],faction["Influence"] * 100,factionstatelng,mode)

        this.gpl.update_window()
