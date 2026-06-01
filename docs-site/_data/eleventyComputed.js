// Set defaults for every file Eleventy renders.
//
// - Apply the `page.html` layout to every Markdown file that does not
//   already declare one in its front matter.
// - Generate pretty URLs so that `schema-1.0/gpg-45/01-introduction.md`
//   becomes `/schema-1.0/gpg-45/01-introduction/` and README.md files become
//   directory-index pages.

module.exports = {
  layout: (data) => data.layout || "page.html",
  permalink: (data) => {
    if (data.permalink) return data.permalink;
    if (data.page.inputPath.endsWith(".md")) {
      const rel = data.page.filePathStem
        .replace(/^\/\.\./, "")
        .replace(/^\//, "");
      if (rel.endsWith("/README") || rel === "README") {
        const stripped = rel.replace(/\/?README$/, "");
        return stripped ? `/${stripped}/` : "/";
      }
      return `/${rel}/`;
    }
    return false;
  },
};
