document.querySelectorAll('li').forEach(item => {
    item.addEventListener('click', () => {
        item.classList.add('pressed');
        setTimeout(() => {
            item.classList.remove('pressed');
        }, 100);
    });
});