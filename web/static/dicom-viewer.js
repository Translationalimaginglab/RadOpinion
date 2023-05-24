var dwvApps = [];
var n_dicoms, n_loadedDicoms, drawable_dicom;
var loadendPromiseResolve;
const loadendPromise = new Promise((resolve, reject) => {
    loadendPromiseResolve = resolve;
});
const DEFAULT_WIDTH = parseInt(getComputedStyle(document.querySelector('.layerGroup')).width);
const DEFAULT_HEIGHT = parseInt(getComputedStyle(document.querySelector('.layerGroup')).height);

function init_dwvApps(dicomURLs) {
    n_dicoms = dicomURLs.length;
    n_loadedDicoms = 0;
    for (let i in dicomURLs) {
        let appOptions = {
            dataViewConfigs: {"*": [{divId: "layerContainer" + i}]},
            tools: {
                Scroll: {},
                WindowLevel: {},
                Filter: {},
                Draw: {
                    type: "factory",
                    options: ["Ruler", "Arrow", "Protractor", "Circle", "Rectangle", "FreeHand"],
                    events: ['drawcreate', 'drawchange', 'drawmove', 'drawdelete'],
                },
            },
        }
        let dwvApp = new dwv.App();
        dwvApp.init(appOptions);
        dwvApp.addEventListener("loadend", dwvApp_onLoadend.bind(event, dwvApp));
        dwvApp.addEventListener("positionchange", dwvApp_onPositionchange.bind(event, dwvApp));
        for (let drawevent of appOptions.tools.Draw.events)
            dwvApp.addEventListener(drawevent, dwvApp_onDrawevent.bind(event, dwvApp));
        dwvApp.loadURLs(dicomURLs[i]);
        dwvApps.push(dwvApp);
    }
}

function dwvApp_onLoad(dwvApp, event) {
    const DEFAULT_WIDTH = dwvApp.getImage(0).getGeometry().getSize().get2D().x;
    const DEFAULT_HEIGHT = dwvApp.getImage(0).getGeometry().getSize().get2D().y;
}

function dwvApp_onLoadend(dwvApp, event) {
    if (++n_loadedDicoms == n_dicoms)
        loadendPromiseResolve("All dicoms are loaded.");
}

function dwvApp_onPositionchange(dwvApp, event) {
    let vc = dwvApp.getLayerGroupById(0).getActiveViewLayer().getViewController();
    let currentIndex = vc.getCurrentIndex().getValues()[2];
    for (let app of dwvApps)
        if (chkTogether.checked) {
            let vc = app.getLayerGroupById(0).getActiveViewLayer().getViewController();
            let values = vc.getCurrentIndex().getValues();
            values[2] = currentIndex;
            vc.setCurrentIndex(new dwv.math.Index(values));
        }
}

function dwvApp_onDrawevent(dwvApp, event) {
    if (dwvApp.getDrawDisplayDetails().length > 0) {
        let item = dwvApp.getDrawDisplayDetails().at(-1);
        form1["answer"].value = item.meta.quantification.length.value;
    } else
        form1["answer"].value = "";
}

function zoom_onChange(event) {
    console.log('zoom change');
    outZoom.value = rngZoom.value + "%";
    let new_zoom = rngZoom.value / 100;
    for (let i in dicomURLs) {
        let layerContainer = document.getElementById("layerContainer" + i);
        layerContainer.style.width = new_zoom * DEFAULT_WIDTH + "px";
        layerContainer.style.height = new_zoom * DEFAULT_HEIGHT + "px";
        dwvApps[i].fitToContainer();
    }
}

function zoom_reset() {
    rngZoom.value = 100;
    zoom_onChange();
}


function reset_display() {
    for (let app of dwvApps)
        app.resetDisplay();
}

function clear_drawings() {
    dwvApps[drawable_dicom].deleteDraws();
}

function set_drawings(drawing_state) {
    for (let app of dwvApps)
        app.deleteDraws();
    if (drawing_state != null) {
        let state = new dwv.io.State();
        let jsonData = new dwv.io.State().fromJSON(drawing_state);
        dwvApps[drawable_dicom].setDrawings(jsonData.drawings, jsonData.drawingsDetails);
    }
}

function tool_onChange(event) {
    let tool = document.querySelector('input[name="radioTool"]:checked').id;
    if (tool == "Draw") {
        for (app of dwvApps)
            app.setTool("Filter");
        dwvApps[drawable_dicom].setTool("Draw");
        dwvApps[drawable_dicom].setDrawShape("Ruler");
    } else
        for (app of dwvApps)
            app.setTool(tool);
}