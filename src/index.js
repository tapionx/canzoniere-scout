document.addEventListener("DOMContentLoaded", function() {
    let pageHeight = 1530;
    let pageWidth = 1100;
    let ratio = 1.41; // height 210mm / width 148.5mm
    let fontStep = 0.5;
    const songs = document.querySelectorAll('.song');
    songs.forEach(song => {
        console.log(song);
        let fontSize = parseFloat(window.getComputedStyle(song).fontSize); 
        const lyrics = song.querySelector('.lyrics');
        if ((song.clientHeight / song.clientWidth) > ratio ){
            // more tall than wide
            while (song.clientHeight < pageHeight) {
                fontSize += fontStep;
                lyrics.style.fontSize = fontSize + 'px';
                console.log("A", song.clientHeight, pageHeight, fontSize);
            }
            while (song.clientHeight > pageHeight) {
                fontSize -= fontStep;
                lyrics.style.fontSize = fontSize + 'px';
                console.log("B", song.clientHeight, pageHeight, fontSize);
            }
            if (song.clientWidth < pageWidth / 2) {
                lyrics.classList.add('columns');
                while (song.clientWidth < pageWidth) {
                    fontSize += fontStep;
                    lyrics.style.fontSize = fontSize + 'px';
                    console.log("1C", song.clientWidth, pageWidth, fontSize);
                }
                while (song.clientWidth > pageWidth) {
                    fontSize -= fontStep;
                    lyrics.style.fontSize = fontSize + 'px';
                    console.log("1D", song.clientWidth, pageWidth, fontSize);
                }
            }
        } else {
            // more wide than tall
            while (song.clientWidth < pageWidth) {
                fontSize += fontStep;
                lyrics.style.fontSize = fontSize + 'px';
                console.log("C", song.clientWidth, pageWidth, fontSize);
            }
            while (song.clientWidth > pageWidth) {
                fontSize -= fontStep;
                lyrics.style.fontSize = fontSize + 'px';
                console.log("D", song.clientWidth, pageWidth, fontSize);
            }
        }
    });
});