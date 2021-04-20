<script src="https://unpkg.com/mermaid@8.6.4/dist/mermaid.min.js"></script>
<script>
// Optional config
// If your document is not specifying `data-md-color-scheme` for color schemes,
// you just need to specify `default`.
window.mermaidConfig = {
  default: {
    startOnLoad: false,
    theme: "default",
    flowchart: {
      htmlLabels: false
    },
    er: {
      useMaxWidth: false
    },
    sequence: {
      useMaxWidth: false
      // Mermaid handles Firefox a little different.
      // For some reason, it doesn't attach font sizes to the labels in Firefox.
      // If we specify the documented defaults, font sizes are written to the labels in Firefox.
      noteFontWeight: "14px",
      actorFontSize: "14px",
      messageFontSize: "16px"
    }
  },

  slate: {
    startOnLoad: false,
    theme: "dark",
    flowchart: {
      htmlLabels: false
    },
    er: {
      useMaxWidth: false
    },
    sequence: {
      useMaxWidth: false,
      noteFontWeight: "14px",
      actorFontSize: "14px",
      messageFontSize: "16px"
    }
  }
}
</script>
<script>
// The loader from "Custom Loader" should go here.
</script>
