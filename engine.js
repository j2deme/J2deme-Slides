const container = require("markdown-it-container");
const deflist = require("markdown-it-deflist");
const { default: markdownItShiki } = require("markdown-it-shiki");

function iconPlugin(md) {
  md.inline.ruler.push("icon", (state, silent) => {
    const src = state.src.slice(state.pos);
    const match = src.match(/^:icon:([a-zA-Z0-9-_]+):(?:\{([^}]+)\})?/);

    if (!match) {
      return false;
    }

    if (!silent) {
      const token = state.push("icon", "i", 0);
      token.content = match[1];
      token.attrs = [];

      if (match[2]) {
        token.attrs.push(["class", match[2]]); // Directly add the class attribute
      }
      token.markup = match[0];
    }

    state.pos += match[0].length;
    return true;
  });

  md.renderer.rules.icon = (tokens, idx) => {
    const token = tokens[idx];

    let classString = `ti ti-${token.content}`;
    if (token.attrs && token.attrs.length > 0) {
      classString += ` ${token.attrs[0][1]}`; // Append the classes
    }
    return `<i class="${classString}"></i>`;
  };
}

function notePlugin(md) {
  md.inline.ruler.push("note", (state, silent) => {
    const src = state.src.slice(state.pos);
    const match = src.match(/^\[\*:([^\]]+)\]/);

    if (!match) {
      return false;
    }

    if (!silent) {
      const token = state.push("note", "div", 0);
      token.content = match[1];
      token.markup = match[0];
    }

    state.pos += match[0].length;
    return true;
  });

  md.renderer.rules.note = (tokens, idx, slf) => {
    const token = tokens[idx];
    const content = md.renderInline(token.content); // Render inline Markdown

    return `<i class="note">*</i><span class="note">${content}</span>`;
  };
}

function stickyNotePlugin(md) {
  const blockTypes = ["ok", "info", "warning", "danger", "tip"];

  blockTypes.forEach((type) => {
    md.inline.ruler.push(type, (state, silent) => {
      const src = state.src.slice(state.pos);
      const match = src.match(new RegExp(`^\\[${type}:([^\\]]+)\\]`));

      if (!match) {
        return false;
      }

      if (!silent) {
        const token = state.push(type, "div", 0);
        token.content = match[1];
        token.markup = match[0];
      }

      state.pos += match[0].length;
      return true;
    });

    md.renderer.rules[type] = (tokens, idx, slf) => {
      const token = tokens[idx];
      const content = md.renderInline(token.content); // Render inline Markdown

      return `<div class="${type} sticky">${content}</div>`;
    };
  });
}

function blockPlugin(md) {
  const blockTypes = [
    "primary",
    "secondary",
    "ok",
    "info",
    "warning",
    "error",
    "danger",
    "note",
    "quote",
    "flex",
    "left",
    "center",
    "right",
    "top",
    "middle",
    "bottom",
    "column",
    "row",
  ];

  blockTypes.forEach((type) => {
    md.use(container, type, {
      render(tokens, idx) {
        const token = tokens[idx];
        const info = token.info.trim().slice(type.length).trim();
        const extraClasses = info ? ` ${info}` : "";

        if (token.nesting === 1) {
          return `<div class="${type}${extraClasses}">\n`;
        } else {
          return `</div>\n`;
        }
      },
    });
  });
}

function dotPlugin(md) {
  md.inline.ruler.push("dot", (state, silent) => {
    const src = state.src.slice(state.pos);
    const match = src.match(/^\[o(2?-?):#?([0-9a-fA-F]{6}|--[a-zA-Z0-9-_]+)\]/);

    if (!match || !["", "-", "2", "2-"].includes(match[1])) {
      return false;
    }

    if (!silent) {
      const token = state.push("dot", "div", 0);
      token.content = match[2];
      token.markup = match[0];
      token.attrs = [
        [
          "class",
          match[1] === ""
            ? "dot"
            : match[1] === "-"
            ? "dot mini"
            : match[1] === "2"
            ? "box"
            : "box mini",
        ],
      ];
    }

    state.pos += match[0].length;
    return true;
  });

  md.renderer.rules.dot = (tokens, idx) => {
    const token = tokens[idx];
    const color = token.content.startsWith("--")
      ? `var(${token.content})`
      : `#${token.content}`;
    const className = token.attrs[0][1];

    return `<div class="${className}" style="background-color: ${color};"></div>`;
  };
}

module.exports = ({ marp }) =>
  marp
    .use(iconPlugin)
    .use(blockPlugin)
    .use(stickyNotePlugin)
    .use(notePlugin)
    .use(dotPlugin)
    .use(markdownItShiki, {
      theme: "material-theme",
      highlightLines: true,
    })
    .use(deflist)
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
    });
