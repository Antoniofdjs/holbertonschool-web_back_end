export default function guardrail(mathFuction) {
  const queue = [];
  try {
    queue.push(mathFuction());
    queue.push('Guardrail was processed');
  } catch (error) {
    queue.push(error);
    queue.push('Guardrail was processed');
  }
  return queue;
}
