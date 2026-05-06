function folderDepth(folder) {
    return folder.path.split("/").length;
}

module.exports = async (tp, categoryFilter) => {
  const CTF_ROOT = `competition`;
  const vault = tp.app.vault;
  const ctfFolders = vault.getAllLoadedFiles()
    .filter(f => f instanceof tp.obsidian.TFolder && f.path.startsWith(CTF_ROOT + "/") && folderDepth(f) === 2);

  ctfFolders.sort((f1, f2) => f1.name.localeCompare(f2.name));
  let output = `## ${categoryFilter}`;

  for (let folder of ctfFolders) {
    const query = `
\`\`\`dataview
TABLE event, note, solved
FROM "${folder.path}"
WHERE type = "challenge" 
  AND category = "${categoryFilter}"
SORT event ASC
\`\`\`
`;

    output += `\n### ${folder.name}\n${query}\n`
  }

  console.log(output);
  return output;
};