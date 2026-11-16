from aqt import mw
from PyQt6.QtGui import QAction, QKeySequence

def safe_replay_audio():
    # Only trigger audio if Anki's current screen is actively reviewing cards
    if mw.state == "review" and mw.reviewer:
        mw.reviewer.replayAudio()

def setup_shortcut():
    # Create a shortcut action mapped to Ctrl+9 (automatically maps to Cmd+9 on macOS)
    action = QAction(mw)
    action.setShortcut(QKeySequence("Ctrl+9"))
    
    # Connect to our safe wrapper function instead of directly to replayAudio
    action.triggered.connect(safe_replay_audio)
    
    # Register it to Anki's main window so it works globally during reviews
    mw.addAction(action)

# Initialize the shortcut on add-on load
setup_shortcut()
