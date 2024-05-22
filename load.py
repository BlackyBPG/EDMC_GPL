"""
The "German Pilot Lounge" Plugin
+ extendet with functionality to show all factions
"""
import l10n
import functools
from config import config
import myNotebook as nb
import json
import requests

_ = functools.partial(l10n.Translations.translate, context=__file__)

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import sys
import time
from l10n import Locale
import time
import math

this = sys.modules[__name__]  # For holding module globals
this.showgpl = tk.IntVar(value=1)
this.showrep = tk.IntVar(value=1)
this.showpil = tk.IntVar(value=0)

# this.eddnstations = "https://eddb.io/archive/v6/stations.json"
this.eddnfactions = "https://www.edsm.net/api-system-v1/factions?systemName="
# this.eddnsystemsp = "https://eddb.io/archive/v6/systems_populated.json"
this.lastTime = 0
this.lastCheckTime = 0
this.dataLoaded = False

APP_VERSION = "24.05.23_b0018"

COLOR_R_RED = [64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,67,70,73,76,79,82,85,88,91,94,97,100,103,106,109,112,115,118,121,124,127,130,133,136,139,142,145,148,151,154,157,160,163,166,169,172,175,178,181,184,187,190,193,196,199,202,205,208,211,214,214,214,215,215,216,216,216,217,217,218,218,218,219,219,220,220,220,221,221,222,222,222,223,223,224,224,224,225,225,226,226,226,227,227,228,228,228,229,229,230,230,230,231,231,232,232,232,233,233,234,234,234,235,235,236,236,236,237,237,238,238,238,239,239,240,240,240,241,241,242,242,242,243,243,244,244,244,245,245,246,246,246,247,247,248,248,248,249,249,250,250,250,251,251,252,252,252,253,253,254]
COLOR_R_GREEN = [255,254,254,253,253,252,252,251,251,250,250,249,249,248,248,247,247,246,246,245,245,244,244,243,243,242,242,241,241,240,240,239,239,238,238,237,237,236,236,235,235,234,234,233,233,232,232,231,231,230,230,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,251,247,243,239,235,234,232,230,229,227,225,224,222,220,219,217,215,214,212,210,209,207,205,204,202,200,199,197,195,194,192,190,189,187,185,184,182,180,179,177,175,174,172,170,169,167,165,164,162,160,159,157,155,154,152,150,149,147,145,144,142,140,139,137,135,134,132,130,129,127,125,124,122,120,119,117,115,114,112,110,109,107,105,104,102,100,99,97,95,94,92,90,89,87,85,84,82,80,79,77,75,74,72,70,69]
COLOR_R_BLUE = [64,67,70,73,76,79,82,85,88,91,94,97,100,103,106,109,112,115,118,121,124,127,130,133,136,139,142,145,148,151,154,157,160,163,166,169,172,175,178,181,184,187,190,193,196,199,202,205,208,211,214,211,208,205,202,199,196,193,190,187,184,181,178,175,172,169,166,163,160,157,154,151,148,145,142,139,136,133,130,127,124,121,118,115,112,109,106,103,100,97,94,91,88,85,82,79,76,73,70,67,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64]

COLOR_I_RED = [64,68,72,75,79,83,86,90,94,97,101,105,108,112,116,119,123,127,130,134,138,141,145,149,152,156,160,163,167,171,174,178,182,185,189,193,196,200,204,207,211,215,218,222,226,229,233,237,240,244,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248]
COLOR_I_GREEN = [248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,248,244,240,237,233,229,226,222,218,215,211,207,204,200,196,193,189,185,182,178,174,171,167,163,160,156,152,149,145,141,138,134,130,127,123,119,116,112,108,105,101,97,94,90,86,83,79,75,72,68,64]
COLOR_I_BLUE = [64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64]

COLOR_NORM = ("#000000", "#80FFFF", "#80FFFF", "#0018FF", "#FF8000", "#FF8000")

MAX_FACTIONS = 10
DEFAULT_SHOWGPL = 1
DEFAULT_SHOWREP = 1
DEFAULT_SHOWPIL = 0
DEFAULT_SHOWOTH = 1
DEFAULT_SHOWCOL = 1
DEFAULT_GPLINT = 0
DEFAULT_REPALL = 0
NAME_PIL = "Pilots' Federation Local Branch"
NAME_GPL_SHORT = "GPL"
NAME_REPUTATION = "Reputation"

CFG_GPL_SHOW = "gpl_showgpl"
CFG_GPL_COL = "gpl_showcol"
CFG_GPL_PIL = "gpl_showpil"
CFG_GPL_OTH = "gpl_showoth"
CFG_GPL_REP = "gpl_showrep"
CFG_GPL_INT = "gpl_integrated"
CFG_GPL_ALL = "gpl_showallrep"
CFG_DESIGN = "theme"

class Gpl(object):
    """
    The main class for the gpl plugin
    """
    widget_System = []
    widget_Security = []
    widget_Name = []
    widget_State = []
    widget_Desc = []
    widget_Perc = []
    widget_Rep = []
    widget_PercRep = []
    widget_ColorA = []
    widget_ColorB = []
    reputation = 0
    influence = 0
    oldlen = 0
    systemsystem = ""
    systemgov = ""
    systemsecurity = ""
    systemfaction = []
    systemfactioninflu = []
    systemfactionstate = []
    systemfactionmode = []
    systemfactionreputation = []
    showgpl = 1
    showrep = 1
    showpil = 0
    showoth = 1
    showcol = 1
    gplint = 1
    repall = 1
    appdesign = 0
    initializeMe = True
    resStations = []
    resSystemsp = []
    resFactions = []

    def load(self):
        try:
            GPL_INT = config.get_int(CFG_GPL_INT)
        except:
            GPL_INT = DEFAULT_GPLINT

        self.gplint = GPL_INT

        try:
            GPL_ALL = config.get_int(CFG_GPL_ALL)
        except:
            GPL_ALL = DEFAULT_REPALL

        self.repall = GPL_ALL

        try:
            self.appdesign = config.get_int(CFG_DESIGN)
        except:
            self.appdesign = 0

        try:
            GPL_SHOW = config.get_int(CFG_GPL_SHOW)
        except:
            GPL_SHOW = DEFAULT_SHOWGPL

        self.showgpl = GPL_SHOW

        try:
            GPL_REP = config.get_int(CFG_GPL_REP)
        except:
            GPL_REP = DEFAULT_SHOWREP

        self.showrep = GPL_REP

        try:
            GPL_PIL = config.get_int(CFG_GPL_PIL)
        except:
            GPL_PIL = DEFAULT_SHOWPIL

        self.showpil = GPL_PIL

        try:
            GPL_OTH = config.get_int(CFG_GPL_OTH)
        except:
            GPL_OTH = DEFAULT_SHOWOTH

        self.showoth = GPL_OTH

        try:
            GPL_COL = config.get_int(CFG_GPL_COL)
        except:
            GPL_COL = DEFAULT_SHOWCOL

        self.showcol = GPL_COL

        self.influence = 0
        self.oldlen = 0
        self.systemsystem = ""
        self.systemgov = ""
        self.systemsecurity = ""
        self.systemfaction = []
        self.systemfactioninflu = []
        self.systemfactionmode = []
        self.systemfactionreputation = []
        self.initializeMe = True

    def data_systemfaction(self, index, sysfaction, influence, state, mode, reputation, system, gov, secure):
        self.systemsystem = system
        self.systemgov = gov
        self.systemsecurity = secure
        if mode == "RESET":
            self.systemfaction = []
            self.systemfactioninflu = []
            self.systemfactionstate = []
            self.systemfactionmode = []
            self.systemfactionreputation = []
            this.dataLoaded = False
            self.requestUpdates(system)
            x = 1
            while x < MAX_FACTIONS:
                self.widget_Name[x].grid_forget()
                self.widget_State[x].grid_forget()
                self.widget_Desc[x].grid_forget()
                self.widget_Perc[x].grid_forget()
                self.widget_Rep[x].grid_forget()
                self.widget_PercRep[x].grid_forget()
                self.widget_ColorA[x].grid_forget()
                self.widget_ColorB[x].grid_forget()
                x = x + 1

            x = 0

        else:
            if len(self.systemfaction) == 0:
                self.systemfaction.append(sysfaction)
                self.systemfactioninflu.append(influence)
                self.systemfactionstate.append(state)
                self.systemfactionmode.append(mode)
                self.systemfactionreputation.append(reputation)
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
                self.systemfactionreputation.insert(insin, reputation)

        self.update_systemfactions()

    def update_window(self):
        self.update_systemfactions()
        # nextcheck = 24-time.gmtime().tm_hour+12
        # if nextcheck >= 24:
        #     nextcheck = nextcheck-24
        # nextstamp = time.time()-this.lastCheckTime
        # if nextstamp > 86400:
            # check now
        #     this.lastCheckTime = time.time()
        #     this.dataLoaded = False
        # elif nextcheck == 0:
        #     if nextstamp > 86400:
        #         # checknow
        #         this.lastCheckTime = time.time()
        #         this.dataLoaded = False

    def requestUpdates(self, edsmsystem):
        this.lastTime = time.time()
        responseF = requests.get(this.eddnfactions + edsmsystem)
        self.resFactions = responseF.json()
        this.dataLoaded = True

    def getFactionPlayer(self,faction):
        if this.dataLoaded == False:
            return 0
        return [obj for obj in list(self.resFactions["factions"]) if obj["name"] == str(faction)][0]["isPlayer"]

    def getFactionNative(self,faction, system):
        if this.dataLoaded == False:
            return -1
        return str(faction).find(str(system))

    def update_systemfactions(self):
        x = 0
        xd = 0
        self.frame.grid()
        self.widget_System[0].after(0, self.widget_System[0].config, {"text": ">> " + self.systemgov})
        self.widget_Security[0].after(0, self.widget_Security[0].config, {"text": self.systemsecurity + " <<"})
        if len(self.systemfaction) > 0:
            self.oldlen = len(self.systemfaction)
            gplint = self.gplint
            repall = self.repall
            if self.showoth == 0:
                gplint = 0
                repall = 0

            showgpl = self.showgpl
            if gplint == 1:
                showgpl = 0

            showrep = self.showrep
            if repall == 1:
                showrep = 0

            while x < len(self.systemfaction):
                if self.showpil == 0 and self.systemfaction[x] == NAME_PIL:
                    xd = xd + 1
                elif showgpl == 0 and self.systemfactionmode[x] == NAME_GPL_SHORT:
                    xd = xd + 1
                elif showrep == 0 and self.systemfactionmode[x] == NAME_REPUTATION:
                    xd = xd + 1
                elif self.showoth == 0 and not ((self.systemfactionmode[x] == NAME_REPUTATION and showrep == 1) or (self.systemfactionmode[x] == NAME_GPL_SHORT and showgpl == 1)):
                    xd = xd + 1
                else:
                    self.widget_Name[x-xd].grid(row=x-xd+1, column=0, sticky=tk.W)
                    self.widget_State[x-xd].grid(row=x-xd+1, column=1, sticky=tk.E+tk.W, padx=10)
                    if (self.systemfactionmode[x] == NAME_REPUTATION and showrep == 1) or (self.systemfactionmode[x] == NAME_GPL_SHORT and showgpl == 1):
                        self.widget_Name[x-xd]["foreground"] = COLOR_NORM[self.appdesign+3]
                    elif (self.systemfactionmode[x] == "NoneSQ" or self.systemfactionmode[x] == "SYSSQ") and gplint == 1 and self.showgpl == 1:
                        self.widget_Name[x-xd]["foreground"] = COLOR_NORM[self.appdesign+3]
                    else:
                        self.widget_Name[x-xd]["foreground"] = COLOR_NORM[self.appdesign]

                    faction = self.systemfaction[x]
                    system = self.systemsystem
                    native = self.getFactionNative(faction,system)
                    player = self.getFactionPlayer(faction)
                    if native >= 0 or player >= 1:
                        faction = "%s " % faction
                        if native >= 0:
                            faction = "%s%s" % (faction,"[N]")
                        if player >= 1:
                            faction = "%s%s" % (faction,"[P]")
                    if self.systemfactionmode[x] == "SYS" or self.systemfactionmode[x] == "SYSSQ":
                        self.widget_Name[x-xd].after(0, self.widget_Name[x-xd].config, {"text": "! " + faction})
                    else:
                        self.widget_Name[x-xd].after(0, self.widget_Name[x-xd].config, {"text": faction})

                    self.widget_State[x-xd].after(0, self.widget_State[x-xd].config, {"text": self.systemfactionstate[x]})

                    msg = "{}".format(Locale.stringFromNumber(self.systemfactioninflu[x], 3))
                    self.widget_Desc[x-xd].grid(row=x-xd+1, column=3, sticky=tk.E)
                    if self.showcol == 1:
                        red = COLOR_I_RED[int(100 - self.systemfactioninflu[x])]
                        green = COLOR_I_GREEN[int(100 - self.systemfactioninflu[x])]
                        blue = COLOR_I_BLUE[int(100 - self.systemfactioninflu[x])]
                        if self.systemfactionmode[x] == NAME_REPUTATION:
                            red = COLOR_R_RED[int(100 - self.systemfactioninflu[x])]
                            green = COLOR_R_GREEN[int(100 - self.systemfactioninflu[x])]
                            blue = COLOR_R_BLUE[int(100 - self.systemfactioninflu[x])]

                        hexrgb = "#%02x%02x%02x" % (red, green, blue)
                        if self.appdesign > 0:
                            self.widget_Desc[x-xd]["foreground"] = hexrgb
                            self.widget_ColorA[x-xd].grid_forget()
                        else:
                            self.widget_Desc[x-xd]["foreground"] = COLOR_NORM[self.appdesign]
                            self.widget_ColorA[x-xd].grid(row=x-xd+1, column=2, sticky=tk.W)
                            self.widget_ColorA[x-xd]["foreground"] = hexrgb
                            self.widget_ColorA[x-xd]["background"] = hexrgb
                    else:
                        self.widget_ColorA[x-xd].grid_forget()

                    self.widget_Desc[x-xd].after(0, self.widget_Desc[x-xd].config, {"text": msg})

                    self.widget_Perc[x-xd].grid(row=x-xd+1, column=4, sticky=tk.W)

                    if repall == 1 and self.showrep == 1 and not ((self.systemfactionmode[x] == NAME_REPUTATION and showrep == 1) or (self.systemfactionmode[x] == NAME_GPL_SHORT and showgpl == 1)):
                        msg = "{}".format(Locale.stringFromNumber(self.systemfactionreputation[x], 3))
                        self.widget_Rep[x-xd].grid(row=x-xd+1, column=6, sticky=tk.E)
                        red = COLOR_R_RED[int(100 - self.systemfactionreputation[x])]
                        green = COLOR_R_GREEN[int(100 - self.systemfactionreputation[x])]
                        blue = COLOR_R_BLUE[int(100 - self.systemfactionreputation[x])]

                        self.widget_Rep[x-xd]["foreground"] = COLOR_NORM[self.appdesign]
                        if self.showcol == 1:
                            hexrgb = "#%02x%02x%02x" % (red, green, blue)
                            if self.appdesign > 0:
                                self.widget_Rep[x-xd]["foreground"] = hexrgb
                                self.widget_ColorB[x-xd].grid_forget()
                            else:
                                self.widget_ColorB[x-xd].grid(row=x-xd+1, column=5, sticky=tk.W)
                                self.widget_ColorB[x-xd]["foreground"] = hexrgb
                                self.widget_ColorB[x-xd]["background"] = hexrgb

                        self.widget_Rep[x-xd].after(0, self.widget_Rep[x-xd].config, {"text": msg})

                        self.widget_PercRep[x-xd].grid(row=x-xd+1, column=7, sticky=tk.W)
                    else:
                        self.widget_Rep[x-xd].grid_forget()
                        self.widget_PercRep[x-xd].grid_forget()
                        self.widget_ColorB[x-xd].grid_forget()

                x = x + 1

            x = x - xd
            y = x
            while x < MAX_FACTIONS:
                self.widget_Name[x].grid_forget()
                self.widget_State[x].grid_forget()
                self.widget_Desc[x].grid_forget()
                self.widget_Perc[x].grid_forget()
                self.widget_Rep[x].grid_forget()
                self.widget_PercRep[x].grid_forget()
                self.widget_ColorA[x].grid_forget()
                self.widget_ColorB[x].grid_forget()
                x = x + 1

            if y == 0:
                self.frame.grid_remove()

        else:
            while x < MAX_FACTIONS:
                self.widget_Name[x].grid_forget()
                self.widget_State[x].grid_forget()
                self.widget_Desc[x].grid_forget()
                self.widget_Perc[x].grid_forget()
                self.widget_Rep[x].grid_forget()
                self.widget_PercRep[x].grid_forget()
                self.widget_ColorA[x].grid_forget()
                self.widget_ColorB[x].grid_forget()
                x = x + 1

            if self.oldlen > 0:
                self.frame.grid_remove()
                self.oldlen = 0


def plugin_prefs(parent, cmdr, is_beta):
    try:
        this.gpl_int = tk.IntVar(value=config.get_int(CFG_GPL_INT))
    except:
        this.gpl_int = tk.IntVar(value=DEFAULT_GPLINT)

    try:
        this.rep_all = tk.IntVar(value=config.get_int(CFG_GPL_ALL))
    except:
        this.rep_all = tk.IntVar(value=DEFAULT_REPALL)

    try:
        this.gpl_show = tk.IntVar(value=config.get_int(CFG_GPL_SHOW))
    except:
        this.gpl_show = tk.IntVar(value=DEFAULT_SHOWGPL)

    try:
        this.rep_show = tk.IntVar(value=config.get_int(CFG_GPL_REP))
    except:
        this.rep_show = tk.IntVar(value=DEFAULT_SHOWREP)

    try:
        this.pil_show = tk.IntVar(value=config.get_int(CFG_GPL_PIL))
    except:
        this.pil_show = tk.IntVar(value=DEFAULT_SHOWPIL)

    try:
        this.oth_show = tk.IntVar(value=config.get_int(CFG_GPL_OTH))
    except:
        this.oth_show = tk.IntVar(value=DEFAULT_SHOWOTH)

    try:
        this.col_show = tk.IntVar(value=config.get_int(CFG_GPL_COL))
    except:
        this.col_show = tk.IntVar(value=DEFAULT_SHOWCOL)

    this.old_gplint = 0
    this.old_showpil = 0
    this.old_repall = 0

    frame = nb.Frame(parent)
    nb.Label(frame, text="GPL-EDMC Version: {INSTALLED}\n".format(INSTALLED=APP_VERSION)).grid(padx=10, sticky=tk.W)
    this.factionbutton = nb.Checkbutton(frame, text=_("Show other System Factions").encode('iso-8859-1'), variable=this.oth_show, onvalue = 1, offvalue = 0, command=prefs_faction_changed)
    this.factionbutton.grid(padx=10, pady = 3, sticky=tk.W)
    this.pilotbutton = nb.Checkbutton(frame, text=_("Show 'Pilots' Federation Local Branch'-Faction in Factionlist").encode('iso-8859-1'), variable=this.pil_show, onvalue = 1, offvalue = 0, command=prefs_normal_changed)
    this.pilotbutton.grid(padx=25, pady = 1, sticky=tk.W)
    this.extragplbutton = nb.Checkbutton(frame, text=_("Show Extra influence for Own-Faction").encode('iso-8859-1'), variable=this.gpl_show, onvalue = 1, offvalue = 0, command=prefs_faction_changed)
    this.extragplbutton.grid(padx=10, pady = 3, sticky=tk.W)
    this.integratebutton = nb.Checkbutton(frame, text=_("Integrate notice in Factionlist").encode('iso-8859-1'), variable=this.gpl_int, onvalue = 1, offvalue = 0, command=prefs_normal_changed)
    this.integratebutton.grid(padx=25, pady = 1, sticky=tk.W)
    this.reputationbutton = nb.Checkbutton(frame, text=_("Show own reputation").encode('iso-8859-1'), variable=this.rep_show, onvalue = 1, offvalue = 0, command=prefs_faction_changed)
    this.reputationbutton.grid(padx=10, pady = 3, sticky=tk.W)
    this.reforallbutton = nb.Checkbutton(frame, text=_("Show reputation for all factions").encode('iso-8859-1'), variable=this.rep_all, onvalue = 1, offvalue = 0, command=prefs_normal_changed)
    this.reforallbutton.grid(padx=25, pady = 1, sticky=tk.W)
    this.colorizebutton = nb.Checkbutton(frame, text=_("Show colorized percentage values").encode('iso-8859-1'), variable=this.col_show, onvalue = 1, offvalue = 0)
    this.colorizebutton.grid(padx=10, pady = 3, sticky=tk.W)
    prefs_normal_changed()
    prefs_faction_changed()
    return frame


def prefs_normal_changed():
    if this.integratebutton['state'] != tk.DISABLED:
        this.old_gplint = this.gpl_int.get()
    
    if this.pilotbutton['state'] != tk.DISABLED:
        this.old_showpil = this.pil_show.get()
    
    if this.reforallbutton['state'] != tk.DISABLED:
        this.old_repall = this.rep_all.get()

    this.gpl.update_window()


def prefs_faction_changed():
    if this.gpl_show.get() == 0:
        this.integratebutton['state'] = tk.DISABLED
        this.gpl_int.set(0)
    else:
        this.integratebutton['state'] = tk.NORMAL
        this.gpl_int.set(this.old_gplint)

    if this.rep_show.get() == 0:
        this.reforallbutton['state'] = tk.DISABLED
        this.rep_all.set(0)
    else:
        this.reforallbutton['state'] = tk.NORMAL
        this.rep_all.set(this.old_repall)

    if this.oth_show.get() == 0:
        this.pilotbutton['state'] = tk.DISABLED
        this.pil_show.set(0)
        this.reforallbutton['state'] = tk.DISABLED
        this.rep_all.set(0)
        this.integratebutton['state'] = tk.DISABLED
        this.gpl_int.set(0)
    else:
        this.pilotbutton['state'] = tk.NORMAL
        this.pil_show.set(this.old_showpil)

        if this.rep_show.get() == 0:
            this.reforallbutton['state'] = tk.DISABLED
            this.rep_all.set(0)
        else:
            this.reforallbutton['state'] = tk.NORMAL
            this.rep_all.set(this.old_repall)

        if this.gpl_show.get() == 0:
            this.integratebutton['state'] = tk.DISABLED
            this.gpl_int.set(0)
        else:
            this.integratebutton['state'] = tk.NORMAL
            this.gpl_int.set(this.old_gplint)

    this.gpl.update_window()


def prefs_changed(cmdr, is_beta):
    gpl = this.gpl
    gpl.showgpl = this.gpl_show.get()
    gpl.showrep = this.rep_show.get()
    gpl.showpil = this.pil_show.get()
    gpl.showoth = this.oth_show.get()
    gpl.showcol = this.col_show.get()
    gpl.gplint = this.gpl_int.get()
    gpl.repall = this.rep_all.get()
    gpl.appdesign = config.get_int(CFG_DESIGN)
    config.set(CFG_GPL_SHOW, gpl.showgpl)
    config.set(CFG_GPL_REP, gpl.showrep)
    config.set(CFG_GPL_PIL, gpl.showpil)
    config.set(CFG_GPL_OTH, gpl.showoth)
    config.set(CFG_GPL_COL, gpl.showcol)
    config.set(CFG_GPL_INT, gpl.gplint)
    config.set(CFG_GPL_ALL, gpl.repall)
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

    objectsystem = tk.Label(frame, text=">> ", justify=tk.LEFT, foreground="#80FFFF")
    objectsystem.grid(row=0, column=0, sticky=tk.W)
    gpl.widget_System.append(objectsystem)

    objectsecurity = tk.Label(frame, text=" <<", justify=tk.RIGHT, foreground="#FF8000")
    objectsecurity.grid(row=0, column=1, columnspan=7, sticky=tk.E)
    gpl.widget_Security.append(objectsecurity)

    i = 0
    while i < MAX_FACTIONS:
        i = i + 1
        objectname = tk.Label(frame, text="", justify=tk.LEFT, foreground="#80FFFF")
        objectname.grid(row=i, column=0, sticky=tk.W)
        gpl.widget_Name.append(objectname)

        objectdesc = tk.Label(frame, text="", justify=tk.RIGHT)
        objectdesc.grid(row=i, column=1, sticky=tk.W+tk.E, padx=10)
        gpl.widget_State.append(objectdesc)

        objectcolor = tk.Label(frame, text="X", justify=tk.RIGHT)
        objectcolor.grid(row=i, column=2, sticky=tk.E)
        gpl.widget_ColorA.append(objectcolor)

        objectdesc = tk.Label(frame, text="", justify=tk.RIGHT)
        objectdesc.grid(row=i, column=3, sticky=tk.E)
        gpl.widget_Desc.append(objectdesc)

        objectperc = tk.Label(frame, text="%", justify=tk.LEFT)
        objectperc.grid(row=i, column=4, sticky=tk.W)
        gpl.widget_Perc.append(objectperc)

        objectcolor = tk.Label(frame, text="X", justify=tk.RIGHT)
        objectcolor.grid(row=i, column=5, sticky=tk.E)
        gpl.widget_ColorB.append(objectcolor)

        objectrep = tk.Label(frame, text="", justify=tk.RIGHT)
        objectrep.grid(row=i, column=6, sticky=tk.E)
        gpl.widget_Rep.append(objectrep)

        objectpercrep = tk.Label(frame, text="%", justify=tk.LEFT)
        objectpercrep.grid(row=i, column=7, sticky=tk.W)
        gpl.widget_PercRep.append(objectpercrep)


    frame.columnconfigure(0, weight=3)
    frame.columnconfigure(1, weight=3)
    frame.columnconfigure(2, weight=0)
    frame.columnconfigure(3, weight=2)
    frame.columnconfigure(4, weight=1)
    frame.columnconfigure(5, weight=0)
    frame.columnconfigure(6, weight=2)
    frame.columnconfigure(7, weight=1)

    this.spacer = tk.Frame(frame)
    gpl.frame = frame
    gpl.update_window()
    return frame


def dashboard_entry(cmdr, is_beta, entry):
    # this.gpl.update_window()
    return

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
            gov = ""
            secure = ""
            if "SystemGovernment_Localised" in entry:
                gov = entry["SystemGovernment_Localised"]

            if "SystemSecurity_Localised" in entry:
                secure = entry["SystemSecurity_Localised"]

            this.gpl.data_systemfaction(0,"","","","RESET",0,entry["StarSystem"],gov,secure)
            fact = "[]"
            msginflu = 0
            msgrepu = 0
            sysfac = None
            sysfacadd = False
            if "SystemFaction" in entry:
                sysfac = dict(entry["SystemFaction"])

            if "Factions" in entry:
                fact = list(entry["Factions"])
                for i in range(len(fact)):
                    faction = dict(fact[i])
                    msgrepu = faction["MyReputation"]
                    if "SquadronFaction" in faction:
                        msginflu = faction["Influence"] * 100
                        this.gpl.data_systemfaction(i,_("Faction Influence:").encode('iso-8859-1'),msginflu,"",NAME_GPL_SHORT,msgrepu,entry["StarSystem"],gov,secure)
                        this.gpl.data_systemfaction(i,_("Faction Reputation:").encode('iso-8859-1'),msgrepu,"",NAME_REPUTATION,msgrepu,entry["StarSystem"],gov,secure)

                    mode = "None"
                    if sysfac != None:
                        if sysfac["Name"] == faction["Name"]:
                            mode = "SYS"
                            sysfacadd = True

                        if "SquadronFaction" in faction:
                            mode = mode + "SQ"

                    if faction["FactionState"] == "None":
                        this.gpl.data_systemfaction(i,faction["Name"],faction["Influence"] * 100,"",mode,msgrepu,entry["StarSystem"],gov,secure)
                    else:
                        factionstatelng = _(faction["FactionState"]).encode('iso-8859-1')
                        this.gpl.data_systemfaction(i,faction["Name"],faction["Influence"] * 100,factionstatelng,mode,msgrepu,entry["StarSystem"],gov,secure)

                if sysfacadd == False:
                    this.gpl.data_systemfaction(i,sysfac["Name"],0,"","SYS",0,entry["StarSystem"],gov,secure)

            this.gpl.update_window()
