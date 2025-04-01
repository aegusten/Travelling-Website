function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  
  const csrftoken = getCookie('csrftoken');
  const updateUrl = document.getElementById('profileUpdateUrl')?.value;
  
  const countryInput = document.getElementById('countryInput');
  const countryList = document.getElementById('countryList');
  
  countryInput.addEventListener('input', function () {
    const query = countryInput.value.trim();
    fetch(`/api/country-search/?q=${encodeURIComponent(query)}`)
      .then(response => response.json())
      .then(data => {
        countryList.innerHTML = "";
        data.forEach(item => {
          const option = document.createElement('option');
          option.value = item.value;
          option.label = item.label;
          countryList.appendChild(option);
        });
      })
      .catch(err => console.error("Country fetch error:", err));
  });
  
  countryInput.addEventListener('change', function () {
    const selectedCountry = countryInput.value.trim();
    if (selectedCountry && updateUrl) {
      fetch(updateUrl, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrftoken,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          update_type: "country",
          country: selectedCountry
        })
      })
        .then(response => response.json().then(data => ({ status: response.status, data })))
        .then(({ status, data }) => {
          if (status >= 400) {
            alert(data.error || "Error updating country");
          } else {
            console.log("Country updated:", data);
          }
        })
        .catch(err => console.error(err));
    }
  });
  
  const currencyInput = document.getElementById('currencyInput');
  const currencyList = document.getElementById('currencyList');
  
  currencyInput.addEventListener('input', function () {
    const query = currencyInput.value.trim();
    fetch(`/api/currency-search/?q=${encodeURIComponent(query)}`)
      .then(response => response.json())
      .then(data => {
        currencyList.innerHTML = "";
        data.forEach(item => {
          const option = document.createElement('option');
          option.value = item.value;
          option.label = item.label;
          currencyList.appendChild(option);
        });
      })
      .catch(err => console.error("Currency fetch error:", err));
  });
  
  currencyInput.addEventListener('change', function () {
    const selectedCurrency = currencyInput.value.trim();
    if (selectedCurrency && updateUrl) {
      fetch(updateUrl, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrftoken,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          update_type: "currency",
          currency: selectedCurrency
        })
      })
        .then(response => response.json().then(data => ({ status: response.status, data })))
        .then(({ status, data }) => {
          if (status >= 400) {
            alert(data.error || "Error updating currency");
          } else {
            console.log("Currency updated:", data);
          }
        })
        .catch(err => console.error(err));
    }
  });
  