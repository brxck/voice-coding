# Contextual grammar for Visual Studio Code

from aenea import *

import lib.format

mapping = {

    ### Files ###
    "[open] command palette": Key("cs-p"),
    "(open [file] | Go to [tab]) [<text>]": Key("c-p") + Text("%(text)s"),
    "open folder": Key("c-k/3, c-o"),
    "save file": Key("c-s"),
    "save and close": Key("c-s/10, c-w"),
    "new window": Key("cs-n"),
    "new file": Key("c-n"),
    
    ### Search ###
    "search [all] (files | codebase)": Key("cs-f"),
    "find": Key("c-f"),
    "replace": Key("c-h"),
    "find next <n>": Key("f3:%(n)d"),
    "find last <n>": Key("s-f3:%(n)d"),    
    # "(Find | Jump [to]) next <text>": Function(findNthToken, n=1, direction="forward"),
    # "(Find | Jump [to]) previous <text>": Function(findNthToken, n=1, direction="reverse"),

    ### Tabs ###
    "nexta [<n>]": Key("c-pgdown:%(n)d"),
    "prexta [<n>]": Key("c-pgup:%(n)d"),
    "close tab": Key("c-w"),
    "exit preview": Key("space, c-z"),

    ### Navigation ###
    "jump <n>": Key("c-g") + Text("%(n)d") + Key("enter"),
    "go to definition": Key("f12"),
    "go to required definition": Key("c-f12:2, c-right:5, left/50, f12"),
    "go to (top | first line)": Key("c-home"),
    "go to ( bottom | last line)": Key("c-end"),

    ### Editing ###
    "indent [<n>]": Key("c-rbracket"),
    "outdent [<n>]": Key("c-lbracket"),
    "slide [<n>]": Key("c-enter"),
    "slip [<n>]": Key("cs-enter"),
    "comment": Key("c-slash"),
    "block comment": Key("sa-a"),
    "move up <n>": Key("a-up:%(n)d"),
    "move down <n>": Key("a-down:%(n)d"),
    "take [all] others": Key("cs-l"),
    "take next [<n>]": Key("c-d:%(n)d"),
    "scrup [<n>]": Key("a-up:%(n)d"),
    "scrown [<n>]": Key("a-down:%(n)d"),
    "scrup page [<n>]": Key("a-pgup:%(n)d"),
    "scrown page [<n>]": Key("a-pgdown:%(n)d"),

    ### Window ###
    "[(show|toggle)] full screen": Key("f11"),
    "[(show|toggle)] Zen mode": Key("c-k/3, z"),
    "[(show|toggle)] side bar": Key("c-b"),
    "[(show|toggle)] files": Key("cs-e"),
    "[(show|toggle)] git": Key("cs-g"),
    "[(show|toggle)] debug": Key("cs-d"),
    "[(show|toggle)] search": Key("cs-f"),
    "[(show|toggle)] extensions": Key("cs-x"),    
    "split": Key("c-backslash"),
    "focus (term|terminal|one)": Key("c-1"),
    "focus two": Key("c-2"),
    "focus three": Key("c-3"),
    "focus four": Key("c-4"),
    "focus right": Key("cs-pagedown"),    
    "focus left": Key("cs-pageup"),
    "toggle (term|terminal|one)": Key("a-1"),
    "new terminal": Key("cs-1"),
    "split terminal": Key("c-backslash"),
    "open settings": Key("c-comma"),
    "open shortcuts": Key("c-k/3, c-s"),
    "change theme": Key("c-k, c-t"),

    ### Debugging ###
    "[toggle] breakpoint": Key("f9"),
    "step over": Key("f10/50"),
    "step into": Key("f11"),
    "step out [of]": Key("s-f11"),
    "resume": Key("f5"),

}

class CommandRule(MappingRule):
    mapping = mapping

    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 50000)
    ]
    defaults = {
        "n": 1,
    }

vs_context1 = ProxyAppContext(executable="code-oss", title="Visual Studio Code")
vs_context2 = ProxyAppContext(executable="code", title="Visual Studio Code")
vs_context = vs_context1 | vs_context2

grammar = Grammar("vscode", context=vs_context)
grammar.add_rule(CommandRule())
grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None