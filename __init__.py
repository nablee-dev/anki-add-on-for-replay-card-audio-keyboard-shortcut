from aqt import mw
from aqt.qt import QAction, QKeySequence

def safe_replay_audio() -> None:
    if mw.state == "review" and mw.reviewer:
        mw.reviewer.replayAudio()

def setup_shortcut() -> None:
    action = QAction(mw)
    action.setShortcut(QKeySequence("Ctrl+9"))
    action.triggered.connect(safe_replay_audio)
    mw.addAction(action)

setup_shortcut()
