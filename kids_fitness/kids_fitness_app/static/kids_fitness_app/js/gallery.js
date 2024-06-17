document.addEventListener("DOMContentLoaded", function() {
    const images = document.querySelectorAll('.fixed-size');
    const modal = document.createElement('div');
    const modalImg = document.createElement('img');

    modal.classList.add('modal');
    modalImg.classList.add('modal-content');

    modal.appendChild(modalImg);
    document.body.appendChild(modal);

    images.forEach(image => {
        image.addEventListener('click', function() {
            modal.style.display = 'flex';
            setTimeout(() => {
                modal.classList.add('show');
            }, 10);
            modalImg.src = this.src;
            modalImg.style.maxWidth = 'none';
            modalImg.style.maxHeight = 'none';
            modalImg.style.width = 'auto';
            modalImg.style.height = 'auto';
        });
    });

    modal.addEventListener('click', function() {
        modal.classList.remove('show');
        setTimeout(() => {
            modal.style.display = 'none';
        }, 300);
    });

    modalImg.addEventListener('click', function(event) {
        event.stopPropagation(); 
        modal.classList.remove('show');
        setTimeout(() => {
            modal.style.display = 'none';
        }, 300);
    });
});