$('[id^=editor_]').each(function() {
    let number = this.id.split('_').pop();
    let url_pyfile = $('#'+this.id).text()  // Extracting url from the div before Ace layer
    let id_editor = "editor_" + number
    function createACE(id_editor){
        var editor = ace.edit(id_editor, {
            theme: "ace/theme/tomorrow_night_bright",
            mode: "ace/mode/python",
            autoScrollEditorIntoView: true,
            maxLines: 30,
            minLines: 6,
            tabSize: 4,
            printMargin: false   // hide ugly margins...
        });
    }
    window.REPL_ready=createACE(id_editor)           // Creating Ace Editor #id_editor

    if (url_pyfile === '') { 
        let editor = ace.edit(id_editor)
        editor.getSession().setValue('\n\n\n\n\n');  // Creates 6 empty lines for UX
    }
});