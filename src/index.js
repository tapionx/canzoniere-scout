document.addEventListener("DOMContentLoaded", function() {
    let pageHeight = 1500;
    let pageWidth = 1100;
    let ratio = 1.41; // height 210mm / width 148.5mm
    const songs = document.querySelectorAll('.song');
    songs.forEach(song => {
        let fontSize = parseFloat(window.getComputedStyle(song).fontSize); 
        if ((song.clientHeight / song.clientWidth) > ratio ){
            while (song.clientHeight < pageHeight) {
                fontSize += 1;
                song.style.fontSize = fontSize + 'px';
                console.log("A", song.clientHeight, pageHeight);
            }
            while (song.clientHeight > pageHeight) {
                fontSize -= 1;
                song.style.fontSize = fontSize + 'px';
                console.log("B", song.clientHeight, pageHeight);
            }
        } else {
            // more wide than tall
            while (song.clientWidth < pageWidth) {
                fontSize += 1;
                song.style.fontSize = fontSize + 'px';
                console.log("C", song.clientWidth, pageWidth);
            }
            while (song.clientWidth > pageWidth) {
                fontSize -= 1;
                song.style.fontSize = fontSize + 'px';
                console.log("D", song.clientWidth, pageWidth);
            }
        }
    });
});