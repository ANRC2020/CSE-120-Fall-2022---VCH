/**
 * BOTH USE THESE FUNCTIONS
 */
// Return to the Home page
function RedirectHome()
{
location.replace("./home.html");
}
function getPatID()
{
var T = document.getElementById("pat_id").value;
return T;
}


/**
 * REPORT GENERTAION PATH JS SCRIPTS
 */
// Make the "Begin Exam" button visible
function ShowExamButton()
{
    var R = document.getElementById("ExamButton");
    R.style.display = "block";
    var T = document.getElementById("pat_id").value;
    //console.log(T);
    document.getElementById("p_id").innerHTML = "Begin Exam for Patient ID: " + T;
    document.getElementById("patient_id").innerHTML = T;
}

function RedirectHome()
{
    location.replace("./home.html");
}

function ShowReportTypes()
{
    // Make the Report Types visible
    var R = document.getElementById("ReportsDiv");
    R.style.display = "block";

    // Query for the exams based on the patient id
    var p_id = document.getElementById("pat_id").value;
    var request = new XMLHttpRequest();
    var url = "/report/"+p_id+"/exams";
    var listOfExams = "";
    let bool = false;
    request.open("GET", url, true);
    request.send();
    request.onload = () => {
        listOfExams += "<table> <tr> <th> </th> <th> Exam ID </th>  <th> Exam Date </th></tr>";
        var exms = request.responseText;
        bool = true;
        const array = [];
        var t = exms.replaceAll(/[,\\""]/g,"").replaceAll('[','').replaceAll(']','').split(" ");
        ti = 0;
        for(i = 0;i<(t.length);i+=8){
            var x = t.slice(i, i+8);
            array[ti] = x;
            ti++;
        }
        for(i = 0; i<=ti; i++)
        {
            document.getElementById("exam_list").innerHTML = listOfExams;
            listOfExams += ("<tr> <td> <form action='/report/"+ (array[i][1])+"/"+ (array[i][0])+"'}} method='GET'><button type='submit'>Select Exam "+ array[i][0]+" </button> </form> <td>" + array[i][0].toString() + "</td> <td>" + array[i][2].toString() + "</td></tr>");
            
            //listOfExams += ("<tr> <td> <button type='submit' onClick='gen_report("+ array[i][0]+")'>Select Exam "+ array[i][0]+"</button> <td>" + array[i][0].toString() + "</td> <td>" + array[i][2].toString() + "</td></tr>");
 
        }//{{url_for('get_exam_report', "+ (pid=array[i][1])+","+ (exid=array[i][0])+")}}
    } 
     
    listOfExams += "</table>";
    console.log(listOfExams);
    var htmlObject = $(listOfExams);
    document.getElementById("exam_list").innerHTML = htmlObject;
}

function gen_report(exam_id)
{
    var p_id = document.getElementById("pat_id").value;
    var e_id = exam_id;

    var request = new XMLHttpRequest();
    var url = "/report/"+p_id+"/" + e_id;
    
    let bool = false;
    request.open("GET", url, true);
    request.send();
    // request.onload = () => {
    //     var exam = request.responseText;
    //     console.log(exam);
    //     bool = true;
    //     return exam;
    // }
}

function ShowExams(examType)
{
    var E = document.getElementById("ExamsDiv");
    if (examType == '1'){
        document.getElementById("amount_mess").innerHTML = "Select ONE (1) exam";
        
    }
    else{
        document.getElementById("amount_mess").innerHTML = "Select TWO (2) exams";
    }
    E.style.display = "block";

}

function ShowGraphGif()
{
    var R = document.getElementById("gif");
    R.style.display = "block";
    var B = document.getElementById("gifButton");
    B.value = "Hide Graph";
}
//gets single exam report of singular patient
function get_exam(){
    var p_id = 0;//document.getElementById("pat_id").value;
    var e_id = 1;//document.getElementById("pat_id").value;

    var request = new XMLHttpRequest();
    var url = "/report/"+p_id+"/"+e_id;

    let bool = false;
    request.open("GET", url, true);
    request.send();
    request.onload = () => {
        var exam = request.responseText;
        console.log(exam)
        console.log(exam.type)
        bool = true; 
        document.getElementById("max-velocity").innerHTML = exam[4];
        document.getElementById("max-angle").innerHTML = exam[3];
        document.getElementById("strength-class").innerHTML = exam[5];
        return exams;
    }
    if(bool == false){
        document.getElementById("exam").innerHTML = "Cannot Find Name."
    }
}




// VR PATH JS SCRIPTS
