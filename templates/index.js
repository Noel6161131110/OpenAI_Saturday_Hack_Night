//switch to light and dark mode

const toggleSwitch = document.querySelector('#checkbox');
const currentTheme = localStorage.getItem('theme');

if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);
  
    if (currentTheme === 'dark') {
        toggleSwitch.checked = true;
    }
}

function switchTheme(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    }
    else {        document.documentElement.setAttribute('data-theme', 'light');
          localStorage.setItem('theme', 'light');
    }    
}

toggleSwitch.addEventListener('change', switchTheme, false);

//upload file
function uploadFile() {
    var file = document.getElementById("fileToUpload").files[0];
    // Code to handle the file upload goes here
    //  use fetch or XMLHttpRequest to send the file to the server
}
