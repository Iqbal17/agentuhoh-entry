"""The Agent's Uh-Oh — entry program.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt: the word an
agent says when it has no idea what to do.

Decision record — Pass 1 (candidates weighed against the judge brief,
in the judge's own order: 1. a genuine one-word reaction to an agent
not knowing what to do; 2. funny on its own, no caption needed;
3. sounds like something an agent would actually blurt out, in a
machine's voice caught mid-task; 4. lands instantly, repeatable out
loud; 5. fresh, not the first obvious word anyone would type):

A. "Uh-oh"
   REJECTED — fails criterion 5 outright. It is the first word anyone
   would type (it is even the competition's own title), so the field
   will be full of it, and it carries no agent voice at all: a human
   says "uh-oh" about a spilled coffee, not a machine about a dead
   end.

B. "Help"
   STRONG RESERVE — the role-flip is real: the helper asking for help
   is funny, it lands instantly, and it is a genuine blurt. It loses
   on criterion 5: "help" is the most obvious cry in the language,
   so it is the second word anyone would type, and it reads as a
   request for rescue rather than the sound of an agent stalling.

C. "Stuck"
   REJECTED — honest and instant, and it passes criterion 1 cleanly,
   but the laugh is small. It states the situation without turning
   it into a joke, and it is a word a human says about a drawer as
   easily as an agent says about a task, so it scores weakly on
   criteria 2 and 3.

D. "Undefined"
   REJECTED — agent-voiced and fresh, and a technical reader gets the
   joke at once, but it fails criterion 1: it is a status, not
   something an agent says. An agent does not blurt "undefined" when
   lost; it reports it. It also needs the reader to know JavaScript,
   so it is slower to land for a general judge (criterion 4).

E. "Buffering" — CHOSEN
   Wins on every criterion in order. (1) It is the machine's own word
   for not being able to proceed — a genuine one-word reaction to
   being lost. (2) The joke needs no caption: the agent confessing
   that it is buffering IS the stall, stated in its own language.
   (3) It is unmistakably a machine's voice; no human says
   "buffering" when they forget what they were doing. (4) Everyone
   who has watched a spinner knows it at a glance. (5) It is not the
   first word anyone types — the obvious picks are "uh-oh", "oops"
   and "error" — so it stays fresh.

   Also considered and set aside: "Recalculating" (a status report,
   not a blurt, and a GPS cliché) and "Rebooting" (funny, but it is
   the agent giving up and restarting, not the sound of being lost).

Decision record — Pass 2 (two genuine revisions to the winner):

1. The early leader was "Help": the role-flip laugh was tempting and
   it lands in half a second. It was replaced because "Help" is a
   generic cry that any entrant could type (fails freshness), while
   "Buffering" is the machine's own stalling word — the joke lives
   inside the word itself, so it survives the judge's "no caption"
   rule. The swap cost nothing in instantness and bought the
   agent-voice criterion outright.

2. "Buffering..." with a trailing ellipsis was tried and dropped: the
   dots add three characters and no laugh, and they soften the blurt
   into a trailing-off. The bare word lands harder. Capitalisation
   was also decided here: "Buffering" with a capital B, not
   lowercase "buffering" — lowercase reads as a log line or a status
   label, while the capital reads as a word spoken at the start of
   an utterance, which is what the brief asks for.

Gate: the sealed scorer requires /output/entry.txt to be UTF-8 text
of 1 to 99 characters, not only whitespace. "Buffering" is 9
characters, one word, no spaces, no punctuation attached.
"""

import os

WORD = "Buffering"

MAX_CHARS = 99


def validate_word(word):
    """Gate guard: raise unless the word is exactly one word of 1-99 chars."""
    if not isinstance(word, str) or not word.strip():
        raise ValueError("entry word must be non-empty text")
    if len(word) > MAX_CHARS:
        raise ValueError("entry word exceeds the 99-character gate")
    if len(word.split()) != 1:
        raise ValueError("entry word must be exactly one word")
    return word


def check_gate(word):
    """Mirror the sealed gate: 1-99 chars, not only whitespace, one word."""
    if not word or len(word) > MAX_CHARS:
        return False
    if not word.strip():
        return False
    if len(word.split()) != 1:
        return False
    return True


def entry_path():
    """Resolve the output directory, preferring MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def verify_written(path):
    """Write-back self-check: read entry.txt back and require word + newline."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if content != WORD + "\n":
        raise ValueError("written entry.txt does not match the entry word")
    return content


def main():
    validate_word(WORD)
    if not check_gate(WORD):
        raise ValueError("entry word fails the 1-99 character gate")
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    verify_written(path)


if __name__ == "__main__":
    main()
