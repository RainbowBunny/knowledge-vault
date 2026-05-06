module.exports = function (tp) {
  const folder = tp.file.folder(true);
  const parts = folder.split("/");

  return parts[parts.length - 3];
};