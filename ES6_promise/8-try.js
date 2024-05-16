export default function divideFunction(numerator, denominator) {
  try {
    if (denominator === 0) {
      throw new Error('cannot devide by zero');
    }
    return numerator / denominator;
  } catch (error) {
    throw error;
  }
}
