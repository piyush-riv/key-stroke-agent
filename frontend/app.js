let editor = null;


// =====================================================
// WebSocket
// =====================================================

const socket = new WebSocket(
    "ws://127.0.0.1:8000/ws"
);


// =====================================================
// Connection status
// =====================================================

socket.onopen = function () {

    console.log("Connected to KeyStroke Agent");

    document.getElementById(
        "connectionStatus"
    ).textContent = "Connected";

    document.getElementById(
        "statusDot"
    ).style.background = "#4ade80";
};


socket.onclose = function () {

    console.log("Disconnected");

    document.getElementById(
        "connectionStatus"
    ).textContent = "Disconnected";

    document.getElementById(
        "statusDot"
    ).style.background = "#777";
};


socket.onerror = function (error) {

    console.error(
        "WebSocket error:",
        error
    );

    document.getElementById(
        "connectionStatus"
    ).textContent = "Connection Error";

    document.getElementById(
        "statusDot"
    ).style.background = "#ef4444";
};


// =====================================================
// Receive messages from backend
// =====================================================

socket.onmessage = function (message) {

    const data = JSON.parse(
        message.data
    );

    console.log(
        "Agent response:",
        data
    );

    updateUI(data);

    function cleanCoachResponse(text) {
    return text
        .replace(/^#{1,6}\s*/gm, "")
        .replace(/\*\*(.*?)\*\*/g, "$1")
        .replace(/\*(.*?)\*/g, "$1")
        .replace(/^\s*[-*]\s+/gm, "• ")
        .trim();
    }

    if (data.coach_response) {
        showSuggestion(
            cleanCoachResponse(data.coach_response)
        );
    }
};


// =====================================================
// Initialize Monaco
// =====================================================

require.config({

    paths: {
        vs:
            "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.52.2/min/vs"
    }

});


require(
    ["vs/editor/editor.main"],
    function () {

        editor = monaco.editor.create(
            document.getElementById("editor"),
            {
                value:
                    "# Write your Python code here\n\n",

                language:
                    "python",

                theme:
                    "vs-dark",

                automaticLayout:
                    true,

                minimap: {
                    enabled: false
                },

                fontSize:
                    15,

                wordWrap:
                    "on"
            }
        );

        console.log(
            "Monaco Editor initialized"
        );


        // ---------------------------------------------
        // Monaco content changes
        // ---------------------------------------------

        editor.onDidChangeModelContent(
            function (event) {

                console.log(
                    "Code changed"
                );

                console.log(
                    editor.getValue()
                );

            }
        );

    }
);


// =====================================================
// Send event to backend
// =====================================================

function sendEvent(
    eventType,
    characterCount
) {

    if (
        socket.readyState !==
        WebSocket.OPEN
    ) {

        console.log(
            "WebSocket not connected"
        );

        return;
    }


    if (!editor) {

        console.log(
            "Editor not initialized"
        );

        return;
    }


    const event = {

        session_id:
            "session_001",

        timestamp:
            Date.now() / 1000,

        event_type:
            eventType,

        character_count:
            characterCount,

        code:
            editor.getValue(),

        language:
            "python"

    };


    console.log(
        "Sending:",
        event
    );


    socket.send(
        JSON.stringify(event)
    );
}


// =====================================================
// Monaco keyboard detection
// =====================================================

function setupKeyboardDetection() {

    if (!editor) {
        return;
    }


    editor.onKeyDown(
        function (event) {

            const keyCode =
                event.keyCode;

            const KeyCode =
                monaco.KeyCode;


            // -----------------------------------------
            // Backspace
            // -----------------------------------------

            if (
                keyCode ===
                KeyCode.Backspace
            ) {

                sendEvent(
                    "backspace",
                    1
                );

                document.getElementById(
                    "eventStatus"
                ).textContent =
                    "Backspace detected";

                return;
            }


            // -----------------------------------------
            // Delete
            // -----------------------------------------

            if (
                keyCode ===
                KeyCode.Delete
            ) {

                sendEvent(
                    "delete",
                    1
                );

                document.getElementById(
                    "eventStatus"
                ).textContent =
                    "Delete detected";

                return;
            }


            // -----------------------------------------
            // Normal character
            // -----------------------------------------

            if (
                event.browserEvent &&
                event.browserEvent.key &&
                event.browserEvent.key.length === 1 &&
                !event.browserEvent.ctrlKey &&
                !event.browserEvent.metaKey &&
                !event.browserEvent.altKey
            ) {

                sendEvent(
                    "keypress",
                    1
                );

                document.getElementById(
                    "eventStatus"
                ).textContent =
                    "Keypress detected";

            }

        }
    );
}


// =====================================================
// Initialize keyboard detection after Monaco loads
// =====================================================

const waitForEditor = setInterval(

    function () {

        if (editor !== null) {

            clearInterval(
                waitForEditor
            );

            setupKeyboardDetection();

        }

    },

    100
);


// =====================================================
// Paste detection
// =====================================================

document.addEventListener(
    "paste",
    function (event) {

        if (!editor) {
            return;
        }


        const text =
            event.clipboardData.getData(
                "text"
            );


        sendEvent(
            "paste",
            text.length
        );


        document.getElementById(
            "eventStatus"
        ).textContent =
            "Paste detected";

    }
);


// =====================================================
// Update UI from SessionState
// =====================================================

function updateUI(state) {

    // ---------------------------------------------
    // Keystrokes
    // ---------------------------------------------

    if (
        state.total_keystrokes !== undefined
    ) {

        document.getElementById(
            "keystrokes"
        ).textContent =
            state.total_keystrokes;

    }


    // ---------------------------------------------
    // Backspaces
    // ---------------------------------------------

    if (
        state.total_backspaces !== undefined
    ) {

        document.getElementById(
            "backspaces"
        ).textContent =
            state.total_backspaces;

    }


    // ---------------------------------------------
    // Deletes
    // ---------------------------------------------

    if (
        state.total_deletes !== undefined
    ) {

        document.getElementById(
            "deletes"
        ).textContent =
            state.total_deletes;

    }


    // ---------------------------------------------
    // Inserted characters
    // ---------------------------------------------

    if (
        state.total_inserted_characters !== undefined
    ) {

        document.getElementById(
            "inserted"
        ).textContent =
            state.total_inserted_characters;

    }


    // ---------------------------------------------
    // Deleted characters
    // ---------------------------------------------

    if (
        state.total_deleted_characters !== undefined
    ) {

        document.getElementById(
            "deleted"
        ).textContent =
            state.total_deleted_characters;

    }


    // ---------------------------------------------
    // Latency
    // ---------------------------------------------

    if (
        state.last_latency !== null &&
        state.last_latency !== undefined
    ) {

        document.getElementById(
            "latency"
        ).textContent =
            state.last_latency.toFixed(2) + "s";

    }


    // ---------------------------------------------
    // Pause
    // ---------------------------------------------

    document.getElementById(
        "pause"
    ).textContent =
        state.pause_detected
            ? "Yes"
            : "No";


    // ---------------------------------------------
    // Backspace ratio
    // ---------------------------------------------

    if (
        state.backspace_ratio !== undefined
    ) {

        document.getElementById(
            "backspaceRatio"
        ).textContent =
            (
                state.backspace_ratio * 100
            ).toFixed(0) + "%";

    }


    // ---------------------------------------------
    // Struggle score
    // ---------------------------------------------

    if (
        state.struggle_score !== undefined
    ) {

        document.getElementById(
            "struggleScore"
        ).textContent =
            state.struggle_score.toFixed(1);

    }

}


// =====================================================
// Show suggestion
// =====================================================

function showSuggestion(
    suggestion
) {

    const box =
        document.getElementById(
            "suggestionBox"
        );

    const text =
        document.getElementById(
            "suggestionText"
        );


    text.textContent =
        suggestion;


    box.style.display =
        "block";
}