addEventListener("load", bindEvent);

const headers = ["Etternavn", "Fornavn", "Student-Id", "Brukernavn"];

function bindEvent() {
  document.getElementById("form").addEventListener("submit", submit, false);
}

function readCsv(input) {
  const file = input.files[0];

  const reader = new FileReader();
  reader.readAsText(file);

  reader.onload = function (e) {
    const csvData = e.target.result;

    const data = Papa.parse(csvData, { header: true, delimiter: ";" });

    if (headers.every((x) => data.meta.fields.includes(x))) {
      document.getElementById("button").disabled = false;
    }
  };
}

async function submit(e) {
  e.preventDefault();
  const file = document.getElementById("file");

  const reader = new FileReader();
  reader.readAsText(file.files[0]);

  reader.onload = function (event) {
    const csvData = event.target.result;

    const csv = Papa.parse(csvData, { header: true, delimiter: ";" });

    const cookies = document.cookie;
    fetch(`${base_url}/export_grades/combine`, {
      method: "POST",
      headers: {
        "X-CSRFToken": cookies.split("=")[1],
        "Content-Type": "application/json",
      },
      body: JSON.stringify(csv),
    })
      .then((res) => res.blob())
      .then((data) => {
        let a = document.createElement("a");
        a.href = window.URL.createObjectURL(data);
        a.download = "grades.csv";
        a.click();
      });
    document.getElementById("button").disabled = false;
  };
}
