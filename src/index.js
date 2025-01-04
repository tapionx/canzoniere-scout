document.addEventListener("DOMContentLoaded", function() {
    let pageHeight = 1500;
    let pageWidth = 1100;
    let ratio = 1.41; // height 210mm / width 148.5mm
    let fontStep = 0.2;
    const songs = document.querySelectorAll('.song');
    songs.forEach(song => {
        console.log(song);
        let fontSize = parseFloat(window.getComputedStyle(song).fontSize); 
        const lyrics = song.querySelector('.lyrics');
        // first make sure height is in one page
        while (song.clientHeight > pageHeight || lyrics.clientWidth > pageWidth) {
            fontSize -= fontStep;
            lyrics.style.fontSize = fontSize + 'px';
        }
        // now we can calculate if it's worth to use columns
        if ((lyrics.clientWidth < pageWidth / 2) && (song.clientHeight > pageHeight * 0.5)) {
            lyrics.classList.add('columns');
        }
        // now we can increase until the limit
        while (song.clientHeight < pageHeight && lyrics.clientWidth < pageWidth) {
            fontSize += fontStep;
            lyrics.style.fontSize = fontSize + 'px';
        }
    });
});