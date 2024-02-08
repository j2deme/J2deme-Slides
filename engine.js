const container = require("markdown-it-container");
const deflist = require("markdown-it-deflist");

module.exports = ({ marp }) =>
  marp
    .use(({ marpit }) => {
      const { highlighter } = marpit;

      // Override Marp Core's highlighter to wrap each lines by ordered list items
      marpit.highlighter = function (...args) {
        const original = highlighter.apply(this, args);
        const listItems = original
          .split(/\n(?!$)/) // Don't split at the trailing newline
          .map(
            (line) =>
              `<li><span data-marp-line-number></span><span>${line}</span></li>`
          );

        return `<ol>${listItems.join("")}</ol>`;
      };
    })
    .use(container, "error")
    .use(container, "warning")
    .use(container, "info")
    .use(container, "ok")
    .use(container, "primary")
    .use(container, "flex")
    .use(container, "col", {
      render(tokens, idx) {
        const token = tokens[idx];
        var size = token.info.trim().slice("col".length).trim();
        var extras = token.info.trim().slice(size.length).trim();
        size = size.replace(extras, "").trim();
        if (size == "") {
          size = extras;
          extras = "";
        }

        if (token.nesting === 1) {
          return `<div class="w-${size} ${extras.trim()}">\n`;
        } else {
          return `</div>\n`;
        }
      },
    })
    .use(container, "coding", {
      render(tokens, idx) {
        const token = tokens[idx];
        var extras = token.info.trim().slice("coding".length).trim();

        if (token.nesting === 1) {
          return `<div class="text-center text-middle font-bold font-mono font-coding text-7xl mt-10 px-2">\n&lt;Coding Time /&gt;\n</div>\n<br>\n${extras}</div>\n`;
        } else {
          return `<!-- End of coding -->\n`;
        }
      },
    })
    .use(deflist);
