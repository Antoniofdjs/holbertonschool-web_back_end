export default function cleanSet(set, startString) {
  const list = [];
  for (const string of set) {
    if (string.startsWith(startString) && startString !== '') { list.push(string.substring(startString.length)); }
  }
  return list.join('-');
}
