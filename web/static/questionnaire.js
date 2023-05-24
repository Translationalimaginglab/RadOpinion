async function revise_html(data) {
    outUser.value = data["user"];
    prgProgress.max = data.n_all;
    prgProgress.value = data.n_answered;
    outProgress.value = `${data.n_answered}/${data.n_all}`;
    form1["question_number"].value = data.q_item.question.number;
    form1["dicom"].value = data.q_item.dicom;
    outDicom.value = data.q_item.dicom;
    form1["previous"].disabled = (data.order == "first");
    form1["next"].disabled = (data.order == "last");

    divQuestion.innerText = data.q_item.question.text;
    divChoices.innerHTML = "";
    if (data.q_item.question.type == "descriptive")
        divChoices.innerHTML +=
            `<input type=text name="answer" tabindex=1 disabled placeholder="Size" value="${data.q_item.answer}"> mm`;
    else
        for (choice of data.q_item.question.choices)
            divChoices.innerHTML += `<label> <input type=radio name="answer" tabindex=1 ${choice == data.q_item.answer ? "checked" : ""} value="${choice}">
                                        ${choice} </label> <br>`;
    form1["answer"].value = data.q_item.answer;

    // dicom-viewer.js
    drawable_dicom = parseInt(data.q_item.question.drawable_sequence);
    await loadendPromise;
    tool_onChange();
    set_drawings(data.q_item.drawing_state);
    if (rngZoom.value != data.zoom) {
        rngZoom.value = data.zoom;
        outZoom.value = data.zoom + "%";
        zoom_onChange()
    }
}

const btns = document.getElementsByClassName("btn");
[...btns].forEach(btn => btn.addEventListener("click", btn_onClick));

const radios = document.getElementsByName("radioTool");
[...radios].forEach(radio => radio.addEventListener("change", tool_onChange));

rngZoom.onchange = zoom_onChange;

function btn_onClick(event) {
    form1["command"].value = event.target.name;
    form1["drawing_state"].value = dwvApps[drawable_dicom].getState();
    document.body.classList.add("waiting");
    fetch("/ajax/", {method: "POST", body: new FormData(form1),})
        .then(response => response.json())
        .then(data => {
            if (data["login_required"])
                window.location.replace('{% url "login" %}');
            else if (data["reload_required"])
                form1.submit();
            else
                revise_html(data["data"]);
            document.body.classList.remove("waiting");
        });
}