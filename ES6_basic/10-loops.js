export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];
  for (const item of array) {
    let value = item;
    value = appendString + value;
    newArray.push(value);
  }

  return newArray;
}
