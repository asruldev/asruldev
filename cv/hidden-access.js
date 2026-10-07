// Desktop: hold Ctrl/Cmd, press C then V. Mobile: long-press the CV name.
(() => {
  let armedUntil = 0;
  const open = () => { window.location.href = 'cover-letter.html'; };
  document.addEventListener('keydown', event => {
    if (event.target.closest('input, textarea, select, [contenteditable="true"]')) return;
    if (!(event.ctrlKey || event.metaKey) || event.altKey || event.shiftKey || event.repeat) {
      armedUntil = 0;
      return;
    }
    const key = event.key.toLowerCase();
    if (key === 'c') {
      armedUntil = Date.now() + 1500;
    } else if (key === 'v' && Date.now() < armedUntil) {
      event.preventDefault();
      armedUntil = 0;
      open();
    } else {
      armedUntil = 0;
    }
  });
  document.addEventListener('keyup', event => {
    if (event.key === 'Control' || event.key === 'Meta') armedUntil = 0;
  });
  const name = document.querySelector('main h1');
  if (!name) return;
  let timer;
  let start;
  let activated = false;
  const cancel = () => { clearTimeout(timer); timer = undefined; };
  name.addEventListener('pointerdown', event => {
    if (event.pointerType !== 'touch' || !event.isPrimary) return;
    cancel();
    activated = false;
    start = { x: event.clientX, y: event.clientY };
    timer = setTimeout(() => { activated = true; open(); }, 1200);
  });
  name.addEventListener('pointermove', event => {
    if (start && Math.hypot(event.clientX - start.x, event.clientY - start.y) > 12) cancel();
  });
  ['pointerup', 'pointercancel', 'pointerleave'].forEach(type => name.addEventListener(type, cancel));
  name.addEventListener('contextmenu', event => {
    if (timer || activated) event.preventDefault();
  });
})();
