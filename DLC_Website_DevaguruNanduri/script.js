// Font size control
function changeFontSize(option) {
    const body = document.body;
    if (option === -1) {
      body.style.fontSize = "16px";
    } else if (option === 0) {
      body.style.fontSize = "18px";
    } else if (option === 1) {
      body.style.fontSize = "20px";
    }
  }
  
  // Language switch alert
  function changeLanguage(lang) {
    alert(`Language changed to: ${lang}`);
  }
  