document.addEventListener('DOMContentLoaded', function() {
    const countryField = document.getElementById('id_country');
    const cityField = document.getElementById('id_city');
  
    if (countryField && cityField) {
      countryField.addEventListener('change', () => {
        const countryId = countryField.value;
        fetch(`/api/cities/?country_id=${countryId}`)
          .then(response => response.json())
          .then(data => {
            cityField.innerHTML = "";
            data.cities.forEach(city => {
              const option = document.createElement('option');
              option.value = city.id;
              option.textContent = city.name;
              cityField.appendChild(option);
            });
          });
      });
    }
  });
  