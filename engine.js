const container = require("markdown-it-container");
const deflist = require("markdown-it-deflist");
// Note: markdown-it-shiki is loaded lazily below only when not in preview mode.
// This avoids the costly/high-frequency rendering issues when Marp runs in live preview.

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

const tablerIcons = {
  folder:
    '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>',
  file: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M13 2v7h7"/></svg>',
  placeholder:
    '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="1"/><circle cx="12" cy="5" r="1"/><circle cx="12" cy="19" r="1"/></svg>',
  // Add more mappings as needed
};

function renderIcon(type) {
  return tablerIcons[type] || tablerIcons.file; // Fallback to a generic file icon
}

function renderFileTree(items, level = 0) {
  let html = '<div class="file-tree">';
  items.forEach((item) => {
    if (item === "...") {
      // Handle placeholder
      html += `<div class="file-tree-item placeholder" style="padding-left: ${
        level * 20
      }px;">${tablerIcons.placeholder} ...</div>`;
      return;
    }

    const isFolder = item.trim().endsWith("/");
    const icon = isFolder
      ? tablerIcons.folder
      : renderIcon(item.split(".").pop());
    const name = isFolder ? item.slice(0, -1) : item;
    html += `<div class="file-tree-item ${
      isFolder ? "folder" : "file"
    }" style="padding-left: ${level * 20}px;">${icon} ${name}</div>`;

    if (isFolder && item.children) {
      // Recursively render nested items
      html += renderFileTree(item.children, level + 1);
    }
  });
  html += "</div>";
  return html;
}

function parseListTokens(tokens, idx) {
  const items = [];
  let currentToken = tokens[idx + 1]; // Start with the first list item

  while (currentToken && currentToken.type === "list_item_open") {
    const contentToken = currentToken.next;
    if (contentToken && contentToken.type === "inline") {
      const item = {
        name: contentToken.content.trim(),
        children: [],
      };

      // Check for nested lists
      let nextToken = contentToken.next;
      if (nextToken && nextToken.type === "bullet_list_open") {
        item.children = parseListTokens(tokens, tokens.indexOf(nextToken));
      }

      items.push(item.name === "..." ? "..." : item);
    }
    currentToken = currentToken.next.next; // Move to the next list item
  }

  return items;
}

function fileTreePlugin(md) {
  // Capture <tree> tags
  md.renderer.rules.html_block = (tokens, idx, options, env, self) => {
    const token = tokens[idx];
    if (
      token.content.startsWith("<tree>") &&
      token.content.endsWith("</tree>")
    ) {
      // Extract the Markdown list inside the <tree> tag
      const listContent = token.content.slice(6, -7).trim();

      // Parse the Markdown list
      const listTokens = md.parse(listContent, env);
      const items = parseListTokens(listTokens, 0);

      // Render the file tree
      return renderFileTree(items);
    }
    return token.content; // Default behavior for other HTML blocks
  };
}

module.exports = ({ marp }) => {
  // Detect preview/watch mode. Marp CLI commonly uses --preview or --watch;
  // also allow environment variables to force behavior (MARP_PREVIEW or MARP_WATCH).
  const argv = Array.isArray(process.argv) ? process.argv : [];
  const isPreview =
    argv.some(
      (a) =>
        a === "--preview" ||
        a === "--watch" ||
        a === "--server" ||
        a === "--serve"
    ) ||
    process.env.MARP_PREVIEW === "true" ||
    process.env.MARP_WATCH === "true";

  // Base engine with lightweight plugins registered first.
  let engine = marp
    .use(iconPlugin)
    .use(blockPlugin)
    .use(stickyNotePlugin)
    .use(notePlugin)
    .use(dotPlugin);

  // Register markdown-it-shiki only when not in preview mode (e.g., PDF/HTML export).
  if (!isPreview) {
    try {
      // Lazy require to avoid loading heavy module during live preview.
      const { default: markdownItShiki } = require("markdown-it-shiki");
      engine = engine.use(markdownItShiki, {
        theme: "material-theme",
        highlightLines: true,
      });
    } catch (err) {
      // If shiki isn't installed, avoid throwing — fall back silently.
      // Log a warning only when running in interactive dev mode.
      if (process.env.NODE_ENV !== "production") {
        // eslint-disable-next-line no-console
        console.warn(
          "markdown-it-shiki not available: code highlighting with shiki disabled."
        );
      }
    }
  }

  // Continue registering remaining plugins.
  engine = engine
    .use(deflist)
    .use(fileTreePlugin)
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

  return engine;
};
