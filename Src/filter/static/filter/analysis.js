const spinnerBox1 = document.getElementById('spinner-box-1')
const spinnerBox2 = document.getElementById('spinner-box-2')
const spinnerBox3 = document.getElementById('spinner-box-3')
const spinnerBox4 = document.getElementById('spinner-box-4')
const dataListBox1 = document.getElementById('data_list_box_1')
const dataListBox2 = document.getElementById('data_list_box_2')
const starAnalysisButton = document.getElementById('start-analysis')
const AnalysisDataBox = document.getElementById('analysised_data_box')


$("#phenotype_1_select").change(function () {
    const phenotype1 = $("#phenotype_1_select").find("option:selected").text();
    $.ajax({
        type: 'POST',
        url: '/data_1/',
        data: {
            'phenotype1': phenotype1,
            'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (response) {
            const data_01_gender = response.result_1_for_gender
            let html_data_gender = '<option value="">Not specify</option>';
            data_01_gender.forEach(element => {
                html_data_gender += `<option value="${element.sex}">${element.sex}</option>`
            });
            $("#gender_1_select").html(html_data_gender);
            const data_01_geo = response.result_1_for_geo
            let html_data_geo = '<option value="">Not specify</option>';
            data_01_geo.forEach(element => {
                html_data_geo += `<option value="${element.geo_location}">${element.geo_location}</option>`
            });
            $("#geo_1_select").html(html_data_geo);
        }
    });
});

$("#phenotype_2_select").change(function () {
    const phenotype2 = $("#phenotype_2_select").find("option:selected").text();
    $.ajax({
        type: 'POST',
        url: '/data_2/',
        data: {
            'phenotype2': phenotype2,
            'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (response) {
            const data_02_gender = response.result_2_for_gender
            let html_data_2_gender = '<option value="">Not specify</option>';
            data_02_gender.forEach(element_2 => {
                html_data_2_gender += `<option value="${element_2.sex}">${element_2.sex}</option>`
            });
            $("#gender_2_select").html(html_data_2_gender);
            const data_02_geo = response.result_2_for_geo
            let html_data_2_geo = '<option value="">Not specify</option>';
            data_02_geo.forEach(element => {
                html_data_2_geo += `<option value="${element.geo_location}">${element.geo_location}</option>`
            });
            $("#geo_2_select").html(html_data_2_geo);
        }
    });
});

$("#gender_1_select").change(function () {
    const gender1 = $("#gender_1_select").find("option:selected").text();
    const phenotype1 = $("#phenotype_1_select").find("option:selected").text();
    if (gender1 != "Not specify") {
        $.ajax({
            type: 'POST',
            url: '/gender_1/',
            data: {
                'gender1': gender1,
                'phenotype1': phenotype1,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                const gender_01 = response.result_3
                let html_data = '<option value="">Not specify</option>';
                gender_01.forEach(element => {
                    html_data += `<option value="${element.geo_location}">${element.geo_location}</option>`
                });
                $("#geo_1_select").html(html_data);
            }
        });
    }
    else {
        $.ajax({
            type: 'POST',
            url: '/data_1/',
            data: {
                'phenotype1': phenotype1,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                const data_01_geo = response.result_1_for_geo
                let html_data_geo = '<option value="">Not specify</option>';
                data_01_geo.forEach(element => {
                    html_data_geo += `<option value="${element.geo_location}">${element.geo_location}</option>`
                });
                $("#geo_1_select").html(html_data_geo);
            }
        });
    }
});

$("#gender_2_select").change(function () {
    const gender2 = $("#gender_2_select").find("option:selected").text();
    const phenotype2 = $("#phenotype_2_select").find("option:selected").text();
    if (gender2 != "Not specify") {
        $.ajax({
            type: 'POST',
            url: '/gender_2/',
            data: {
                'phenotype2': phenotype2,
                'gender2': gender2,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                const gender_02 = response.result_4
                let html_data = '<option value="">Not specify</option>';
                gender_02.forEach(element => {
                    html_data += `<option value="${element.geo_location}">${element.geo_location}</option>`
                });
                $("#geo_2_select").html(html_data);
            }
        });
    }
    else {
        $.ajax({
            type: 'POST',
            url: '/data_2/',
            data: {
                'phenotype2': phenotype2,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                const data_02_geo = response.result_2_for_geo
                let html_data_2_geo = '<option value="">Not specify</option>';
                data_02_geo.forEach(element => {
                    html_data_2_geo += `<option value="${element.geo_location}">${element.geo_location}</option>`
                });
                $("#geo_2_select").html(html_data_2_geo);
            }
        });
    }
});


$("#submit-1").click(function () {
    const phenotype1 = $("#phenotype_1_select").find("option:selected").text();
    const phenotype2 = $("#phenotype_2_select").find("option:selected").text();
    if (phenotype1 != "Choose Phenotype #1 (required)" && phenotype2 != "Choose Phenotype #2 (required)") {
        spinnerBox1.classList.remove('not-visible')
        dataListBox1.classList.add('not-visible')
        const gender1 = $("#gender_1_select").find("option:selected").text();
        const geo1 = $("#geo_1_select").find("option:selected").text();
        const age1Bottom = $("#age1-bottom").val();
        const age1Top = $("#age1-top").val();
        const bmi1Bottom = $("#bmi1-bottom").val();
        const bmi1Top = $("#bmi1-top").val();
        $.ajax({
            type: 'POST',
            url: '/submit_1/',
            data: {
                'phenotype1': phenotype1,
                'gender1': gender1,
                'geo1': geo1,
                'age1Bottom': age1Bottom,
                'age1Top': age1Top,
                'bmi1Bottom': bmi1Bottom,
                'bmi1Top': bmi1Top,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                dataListBox1.classList.remove('not-visible')
                AnalysisDataBox.classList.add('not-visible')
                const list_final = response.list_final
                let table_col = `
                    <div class="card mb-3 mt-3 mx-3">
                        <div class="card-body table-responsive">
                            <div id="toolbar" class="select">
                                <select class="form-control">
                                    <option value="">Export Basic</option>
                                    <option value="all">Export All</option>
                                    <option value="selected">Export Selected</option>
                                </select>
                            </div>
                            <table id="table"
                            data-toggle="table"
                            data-height="485"
                            data-search="true"
                            data-toolbar="#toolbar"
                            data-show-export="true"
                            data-show-search-clear-button="true"
                            data-pagination="true"
                            class="table table-sm table-striped">
                                * 0 in column Age & BMI represent no record
                                <thead>
                                    <tr>
                                        <th scope="col" data-sortable="true">Run ID</th>
                                        <th scope="col" data-sortable="true">Gender</th>
                                        <th scope="col" data-sortable="true">Age</th>
                                        <th scope="col" data-sortable="true">BMI</th>
                                        <th scope="col" data-sortable="true">Geo location</th>
                                        <th scope="col" data-sortable="true">SRA study</th>
                                        <th scope="col" data-sortable="true">Bio project</th>
                                        <th scope="col" data-sortable="true">Bio sample</th>
                                        <th scope="col" data-sortable="true">Library layout</th>
                                        <th scope="col" data-sortable="true">Platform</th>
                                        <th scope="col" data-sortable="true">Model</th>
                                    </tr>
                                </thead>
                                <tbody>
                `;
                list_final.forEach(element => {
                    table_col += `
                        <tr>
                            <th scope="row">${element.run}</th>
                            <td>${element.sex}</td>
                            <td>${element.age}</td>
                            <td>${element.bmi}</td>
                            <td>${element.geo_location}</td>
                            <td>${element.srastudy}</td>
                            <td>${element.bioproject}<a href="https://www.ncbi.nlm.nih.gov/bioproject/${element.bioproject}/" target="_blank"><i class="bi bi-box-arrow-in-right"></i></a></td>
                            <td>${element.biosample}</td>
                            <td>${element.librarylayout}</td>
                            <td>${element.platform}</td>
                            <td>${element.model}</td>
                        </tr>
                        `
                });
                table_col += `
                                </tbody>
                            </table>
                        </div>
                    </div>
                `;
                dataListBox1.innerHTML = (table_col);
                $('[data-toggle="table"]').bootstrapTable();
                spinnerBox1.classList.add('not-visible')
                starAnalysisButton.classList.remove('not-visible')
            }
        });
    }
    else if (phenotype1 != "Choose Phenotype #1 (required)") {
        spinnerBox1.classList.remove('not-visible')
        dataListBox1.classList.add('not-visible')
        const gender1 = $("#gender_1_select").find("option:selected").text();
        const geo1 = $("#geo_1_select").find("option:selected").text();
        const age1Bottom = $("#age1-bottom").val();
        const age1Top = $("#age1-top").val();
        const bmi1Bottom = $("#bmi1-bottom").val();
        const bmi1Top = $("#bmi1-top").val();
        $.ajax({
            type: 'POST',
            url: '/submit_1/',
            data: {
                'phenotype1': phenotype1,
                'gender1': gender1,
                'geo1': geo1,
                'age1Bottom': age1Bottom,
                'age1Top': age1Top,
                'bmi1Bottom': bmi1Bottom,
                'bmi1Top': bmi1Top,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                dataListBox1.classList.remove('not-visible')
                AnalysisDataBox.classList.add('not-visible')
                const list_final = response.list_final
                let table_col = `
                    <div class="card mb-3 mt-3 mx-3">
                        <div class="card-body table-responsive">
                            <div id="toolbar" class="select">
                                <select class="form-control">
                                    <option value="">Export Basic</option>
                                    <option value="all">Export All</option>
                                    <option value="selected">Export Selected</option>
                                </select>
                            </div>
                            <table id="table"
                            data-toggle="table"
                            data-height="485"
                            data-search="true"
                            data-toolbar="#toolbar"
                            data-show-export="true"
                            data-show-search-clear-button="true"
                            data-pagination="true"
                            class="table table-sm table-striped">
                                * 0 in column Age & BMI represent no record
                                <thead>
                                    <tr>
                                        <th scope="col" data-sortable="true">Run ID</th>
                                        <th scope="col" data-sortable="true">Gender</th>
                                        <th scope="col" data-sortable="true">Age</th>
                                        <th scope="col" data-sortable="true">BMI</th>
                                        <th scope="col" data-sortable="true">Geo location</th>
                                        <th scope="col" data-sortable="true">SRA study</th>
                                        <th scope="col" data-sortable="true">Bio project</th>
                                        <th scope="col" data-sortable="true">Bio sample</th>
                                        <th scope="col" data-sortable="true">Library layout</th>
                                        <th scope="col" data-sortable="true">Platform</th>
                                        <th scope="col" data-sortable="true">Model</th>
                                    </tr>
                                </thead>
                                <tbody>
                `;
                list_final.forEach(element => {
                    table_col += `
                        <tr>
                            <th scope="row">${element.run}</th>
                            <td>${element.sex}</td>
                            <td>${element.age}</td>
                            <td>${element.bmi}</td>
                            <td>${element.geo_location}</td>
                            <td>${element.srastudy}</td>
                            <td>${element.bioproject}<a href="https://www.ncbi.nlm.nih.gov/bioproject/${element.bioproject}/" target="_blank"><i class="bi bi-box-arrow-in-right"></i></a></td>
                            <td>${element.biosample}</td>
                            <td>${element.librarylayout}</td>
                            <td>${element.platform}</td>
                            <td>${element.model}</td>
                        </tr>
                        `
                });
                table_col += `
                                </tbody>
                            </table>
                        </div>
                    </div>
                `;
                dataListBox1.innerHTML = (table_col);
                $('[data-toggle="table"]').bootstrapTable();
                spinnerBox1.classList.add('not-visible')
            }
        });
    }
    else {
        window.alert('Please select phenotype !');
    }
});

$("#submit-2").click(function () {
    const phenotype1 = $("#phenotype_1_select").find("option:selected").text();
    const phenotype2 = $("#phenotype_2_select").find("option:selected").text();
    if (phenotype1 != "Choose Phenotype #1 (required)" && phenotype2 != "Choose Phenotype #2 (required)") {
        spinnerBox2.classList.remove('not-visible')
        dataListBox2.classList.add('not-visible')
        const gender2 = $("#gender_2_select").find("option:selected").text();
        const geo2 = $("#geo_2_select").find("option:selected").text();
        const age2Bottom = $("#age2-bottom").val();
        const age2Top = $("#age2-top").val();
        const bmi2Bottom = $("#bmi2-bottom").val();
        const bmi2Top = $("#bmi2-top").val();
        $.ajax({
            type: 'POST',
            url: '/submit_2/',
            data: {
                'phenotype2': phenotype2,
                'gender2': gender2,
                'geo2': geo2,
                'age2Bottom': age2Bottom,
                'age2Top': age2Top,
                'bmi2Bottom': bmi2Bottom,
                'bmi2Top': bmi2Top,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                dataListBox2.classList.remove('not-visible')
                AnalysisDataBox.classList.add('not-visible')
                const list_final = response.list_final
                let table_col = `
                    <div class="card mb-3 mt-3 mx-3">
                        <div class="card-body table-responsive">
                            <div id="toolbar-2" class="select">
                                <select class="form-control">
                                    <option value="">Export Basic</option>
                                    <option value="all">Export All</option>
                                    <option value="selected">Export Selected</option>
                                </select>
                            </div>
                            <table id="table"
                            data-toggle="table"
                            data-height="485"
                            data-search="true"
                            data-toolbar="#toolbar-2"
                            data-show-export="true"
                            data-show-search-clear-button="true"
                            data-pagination="true"
                            class="table table-sm table-striped">
                                * 0 in column Age & BMI represent no record
                                <thead>
                                    <tr>
                                        <th scope="col" data-sortable="true">Run ID</th>
                                        <th scope="col" data-sortable="true">Gender</th>
                                        <th scope="col" data-sortable="true">Age</th>
                                        <th scope="col" data-sortable="true">BMI</th>
                                        <th scope="col" data-sortable="true">Geo location</th>
                                        <th scope="col" data-sortable="true">SRA study</th>
                                        <th scope="col" data-sortable="true">Bio project</th>
                                        <th scope="col" data-sortable="true">Bio sample</th>
                                        <th scope="col" data-sortable="true">Library layout</th>
                                        <th scope="col" data-sortable="true">Platform</th>
                                        <th scope="col" data-sortable="true">Model</th>
                                    </tr>
                                </thead>
                                <tbody>
                `;
                list_final.forEach(element => {
                    table_col += `
                        <tr>
                            <th scope="row">${element.run}</th>
                            <td>${element.sex}</td>
                            <td>${element.age}</td>
                            <td>${element.bmi}</td>
                            <td>${element.geo_location}</td>
                            <td>${element.srastudy}</td>
                            <td>${element.bioproject}<a href="https://www.ncbi.nlm.nih.gov/bioproject/${element.bioproject}/" target="_blank"><i class="bi bi-box-arrow-in-right"></i></a></td>
                            <td>${element.biosample}</td>
                            <td>${element.librarylayout}</td>
                            <td>${element.platform}</td>
                            <td>${element.model}</td>
                        </tr>
                        `
                });
                table_col += `
                                </tbody>
                            </table>
                        </div>
                    </div>
                `;
                dataListBox2.innerHTML = (table_col);
                $('[data-toggle="table"]').bootstrapTable();
                spinnerBox2.classList.add('not-visible')
                starAnalysisButton.classList.remove('not-visible')
            }
        });
    }
    else if (phenotype2 != "Choose Phenotype #2 (required)") {
        spinnerBox2.classList.remove('not-visible')
        dataListBox2.classList.add('not-visible')
        const gender2 = $("#gender_2_select").find("option:selected").text();
        const geo2 = $("#geo_2_select").find("option:selected").text();
        const age2Bottom = $("#age2-bottom").val();
        const age2Top = $("#age2-top").val();
        const bmi2Bottom = $("#bmi2-bottom").val();
        const bmi2Top = $("#bmi2-top").val();
        $.ajax({
            type: 'POST',
            url: '/submit_2/',
            data: {
                'phenotype2': phenotype2,
                'gender2': gender2,
                'geo2': geo2,
                'age2Bottom': age2Bottom,
                'age2Top': age2Top,
                'bmi2Bottom': bmi2Bottom,
                'bmi2Top': bmi2Top,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                dataListBox2.classList.remove('not-visible')
                AnalysisDataBox.classList.add('not-visible')
                const list_final = response.list_final
                let table_col = `
                    <div class="card mb-3 mt-3 mx-3">
                        <div class="card-body table-responsive">
                            <div id="toolbar-2" class="select">
                                <select class="form-control">
                                    <option value="">Export Basic</option>
                                    <option value="all">Export All</option>
                                    <option value="selected">Export Selected</option>
                                </select>
                            </div>
                            <table id="table"
                            data-toggle="table"
                            data-height="485"
                            data-search="true"
                            data-toolbar="#toolbar-2"
                            data-show-export="true"
                            data-show-search-clear-button="true"
                            data-pagination="true"
                            class="table table-sm table-striped">
                                * 0 in column Age & BMI represent no record
                                <thead>
                                    <tr>
                                        <th scope="col" data-sortable="true">Run ID</th>
                                        <th scope="col" data-sortable="true">Gender</th>
                                        <th scope="col" data-sortable="true">Age</th>
                                        <th scope="col" data-sortable="true">BMI</th>
                                        <th scope="col" data-sortable="true">Geo location</th>
                                        <th scope="col" data-sortable="true">SRA study</th>
                                        <th scope="col" data-sortable="true">Bio project</th>
                                        <th scope="col" data-sortable="true">Bio sample</th>
                                        <th scope="col" data-sortable="true">Library layout</th>
                                        <th scope="col" data-sortable="true">Platform</th>
                                        <th scope="col" data-sortable="true">Model</th>
                                    </tr>
                                </thead>
                                <tbody>
                `;
                list_final.forEach(element => {
                    table_col += `
                        <tr>
                            <th scope="row">${element.run}</th>
                            <td>${element.sex}</td>
                            <td>${element.age}</td>
                            <td>${element.bmi}</td>
                            <td>${element.geo_location}</td>
                            <td>${element.srastudy}</td>
                            <td>${element.bioproject}<a href="https://www.ncbi.nlm.nih.gov/bioproject/${element.bioproject}/" target="_blank"><i class="bi bi-box-arrow-in-right"></i></a></td>
                            <td>${element.biosample}</td>
                            <td>${element.librarylayout}</td>
                            <td>${element.platform}</td>
                            <td>${element.model}</td>
                        </tr>
                        `
                });
                table_col += `
                                </tbody>
                            </table>
                        </div>
                    </div>
                `;
                dataListBox2.innerHTML = (table_col);
                $('[data-toggle="table"]').bootstrapTable();
                spinnerBox2.classList.add('not-visible')
            }
        });
    }
    else {
        window.alert('Please select phenotype !');
    }
});


$("#start-analysis").click(function () {
    spinnerBox3.classList.remove('not-visible')
    spinnerBox4.classList.remove('not-visible')
    var startTime = 0;
    var intervalId;
        function updateCounter() {
        let currentTime = Date.now();
        let msecond = ("0" + (currentTime - startTime) % 1000).substr(-3, 3);
        let counter = Math.floor((currentTime - startTime)/1000);
        let hour = ("0" + Math.floor(counter / 3600)).substr(-2, 2);
        let minute = ("0" + Math.floor((counter % 3600) / 60)).substr(-2, 2);
        let second = ("0" + Math.floor(counter % 60)).substr(-2, 2);
        document.getElementById('counter').textContent = `${hour} hour ${minute} min${second}.${msecond} sec`;
        }
    startTime = Date.now();
    intervalId = setInterval(updateCounter, 15);
    starAnalysisButton.classList.add('not-visible')
    const phenotype1 = $("#phenotype_1_select").find("option:selected").text();
    const phenotype2 = $("#phenotype_2_select").find("option:selected").text();
    const gender1 = $("#gender_1_select").find("option:selected").text();
    const geo1 = $("#geo_1_select").find("option:selected").text();
    const age1Bottom = $("#age1-bottom").val();
    const age1Top = $("#age1-top").val();
    const bmi1Bottom = $("#bmi1-bottom").val();
    const bmi1Top = $("#bmi1-top").val();
    const gender2 = $("#gender_2_select").find("option:selected").text();
    const geo2 = $("#geo_2_select").find("option:selected").text();
    const age2Bottom = $("#age2-bottom").val();
    const age2Top = $("#age2-top").val();
    const bmi2Bottom = $("#bmi2-bottom").val();
    const bmi2Top = $("#bmi2-top").val();

    $.ajax({
        type: 'POST',
        url: '/start_analysis/',
        data: {
            'phenotype1': phenotype1,
            'gender1': gender1,
            'geo1': geo1,
            'age1Bottom': age1Bottom,
            'age1Top': age1Top,
            'bmi1Bottom': bmi1Bottom,
            'bmi1Top': bmi1Top,
            'phenotype2': phenotype2,
            'gender2': gender2,
            'geo2': geo2,
            'age2Bottom': age2Bottom,
            'age2Top': age2Top,
            'bmi2Bottom': bmi2Bottom,
            'bmi2Top': bmi2Top,
            'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (response) {
            picturePath = response.folderpath
            clearInterval(intervalId)
            AnalysisDataBox.classList.remove('not-visible')
            AnalysisDataBox.innerHTML = `
                <div class="container mt-3 mb-3 text-center">
                    <p class="h1 fw-bold" style="color: #052339;">Result</p>
                </div>
                <div class="card mb-3">
                    <nav>
                        <div class="nav nav-tabs" id="nav-tab" role="tablist">
                            <button class="nav-link fw-bold active" id="nav-1-tab" data-bs-toggle="tab" data-bs-target="#nav-1" type="button" role="tab" aria-controls="nav-1" aria-selected="true">Alpha diversity</button>
                            <button class="nav-link fw-bold" id="nav-2-tab" data-bs-toggle="tab" data-bs-target="#nav-2" type="button" role="tab" aria-controls="nav-2" aria-selected="false">Beta diversity</button>
                            <button class="nav-link fw-bold" id="nav-3-tab" data-bs-toggle="tab" data-bs-target="#nav-3" type="button" role="tab" aria-controls="nav-3" aria-selected="false">Abundance</button>
                        </div>
                    </nav>
                    <div class="tab-content" id="nav-tabContent">
                        <div class="tab-pane fade show active" id="nav-1" role="tabpanel" aria-labelledby="nav-1-tab">
                            <div class="card text-center">
                                <div class="card-body">
                                    <div class="card text-center mt-3 mb-5 mx-3">
                                        <div class="card-header mb-5" style="background-color: #052339; color: white;">Taxanomic annonate to Genus</div>
                                        <img src = "${picturePath}G_alpha_chao1.jpg" width = 80% heigh = 80% border="1" alt = "picture-1" style = "display:block; margin:auto;"/>
                                        <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                        </div>
                                        <img src = "${picturePath}G_alpha_shannon.jpg" width = 80% heigh = 80% border="1" alt = "picture-1" style = "display:block; margin:auto;"/>
                                        <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                        </div>
                                    </div>
                                    <div class="card text-center mt-5 mb-5 mx-3">
                                        <div class="card-header mb-5" style="background-color: #052339; color: white;">Taxanomic annonate to Species</div>
                                        <img src = "${picturePath}S_alpha_chao1.jpg" width = 80% heigh = 80% border="1" alt = "picture-1" style = "display:block; margin:auto;"/>
                                        <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                        </div>
                                        <img src = "${picturePath}S_alpha_shannon.jpg" width = 80% heigh = 80% border="1" alt = "picture-1" style = "display:block; margin:auto;"/>
                                        <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="tab-pane fade" id="nav-2" role="tabpanel" aria-labelledby="nav-2-tab">
                            <div class="card">
                                <div class="card-body">
                                    <div class="card text-center mt-3 mb-5 mx-3">
                                        <div class="card-header mb-5" style="background-color: #052339; color: white;">Taxanomic annonate to Genus</div>
                                        <img src = "${picturePath}G_alpha_chao1.jpg" width = 80% heigh = 80% border="1" alt = "picture-1" style = "display:block; margin:auto;"/>
                                        <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                        </div>
                                        <img src = "${picturePath}G_alpha_shannon.jpg" width = 80% heigh = 80% border="1" alt = "picture-1" style = "display:block; margin:auto;"/>
                                        <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="tab-pane fade" id="nav-3" role="tabpanel" aria-labelledby="nav-3-tab">
                            <div class="card">
                                <div class="card-body">
                                    <div class="card text-center mt-3 mb-5 mx-3">
                                        <div class="card-header mb-5" style="background-color: #052339; color: white;">Taxanomic annonate to Genus</div>
                                        <img src = "${picturePath}G_A+B.png" width = 80% heigh = 80% border="1" alt = "picture-1" style = "display:block; margin:auto;"/>
                                        <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                        </div>
                                        <img src = "${picturePath}G_A+B.cladogram.png" width = 80% heigh = 80% border="1" alt = "picture-1" style = "display:block; margin:auto;"/>
                                        <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                        </div>
                                    </div>
                                    <div class="card text-center mt-3 mb-5 mx-3">
                                        <div class="card-header mb-5" style="background-color: #052339; color: white;">Taxanomic annonate to Genus</div>
                                        <img src = "${picturePath}S_A+B.png" width = 80% heigh = 80% border="1" alt = "picture-1" style = "display:block; margin:auto;"/>
                                        <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                        </div>
                                        <img src = "${picturePath}S_A+B.cladogram.png" width = 80% heigh = 80% border="1" alt = "picture-1" style = "display:block; margin:auto;"/>
                                        <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            `
            spinnerBox3.classList.add('not-visible')
            spinnerBox4.classList.add('not-visible')
        }
    });
})

var $table = $('#table')
$(function() {
    $('#toolbar').find('select').change(function () {
      $table.bootstrapTable('destroy').bootstrapTable({
        exportDataType: $(this).val(),
        exportTypes: ['json', 'xml', 'csv', 'txt', 'sql', 'excel', 'pdf'],
        columns: [
          {
            field: 'state',
            checkbox: true,
            visible: $(this).val() === 'selected'
          },
          {
            field: 'run',
            title: 'Run ID'
          }, {
            field: 'sex',
            title: 'Gender'
          }, {
            field: 'bmi',
            title: 'BMI'
        }, {
            field: 'geo_location',
            title: 'Geo location'
        }, {
            field: 'bmi',
            title: 'BMI'
        }, {
            field: 'srastudy',
            title: 'SRA study'
        }, {
            field: 'bioproject',
            title: 'Item Price'
        }, {
            field: 'biosample',
            title: 'Bio sample'
        }, {
            field: 'librarylayout',
            title: 'Library layout'
        }, {
            field: 'platform',
            title: 'Platform'
        }, {
            field: 'model',
            title: 'Model'
          }
        ]
      })
    }).trigger('change')
  })