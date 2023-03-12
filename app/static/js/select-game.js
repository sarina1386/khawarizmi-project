/*!
	* Toasts
	* 
	* 
*/

var userGrade = 9;
var userLesson = 1;

if (document.readyState == 'loading') 
{
    document.addEventListener('DOMContentLoaded', main)
} 
else 
{
    main()
}

function main() {
    let grades = document.querySelector('#grades');
    let gradeButs = grades.querySelectorAll('button');
    
    for(let i = 0; i < gradeButs.length; i++) {
        gradeButs[i].addEventListener('click', chooseGrade);
    }
    
}

function chooseGrade(e) {
    let chooseGradeDiv = document.querySelector('#choose-grade');
    let chooseLessonDiv = document.querySelector('#choose-lesson');
    let selectedGrade = e.target.parentElement;
    let gradeTitle = selectedGrade.querySelector('.event__title').innerHTML;
    let grade = 9;

    chooseGradeDiv.classList.remove('d-none');
    chooseLessonDiv.classList.add('d-none');

    if(gradeTitle == 'هفتم') {
        grade = 7;
    }
    else if(gradeTitle == 'هشتم') {
        grade = 8;
    }
    
    userGrade = grade;
    chooseLesson(grade);
}

function chooseLesson(grade) {
    let chooseGradeDiv = document.querySelector('#choose-grade');
    let chooseLessonDiv = document.querySelector('#choose-lesson');
    let lessonCard = document.querySelector('#lesson-card');
    let contentError = document.querySelector('#no-content-err');
    let serverError = document.querySelector('#server-err');

    contentError.classList.add('d-none');
    serverError.classList.add('d-none');

    let pigeon = {grade: grade};
    let detail = [];
    let content = [];
    $.ajax({
        type: "POST",
        url: "/api/get-lessons",
        async: false,
        data: JSON.stringify(pigeon),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(result) {
            console.log(result)
            if(result['status'] == 'ok') {
                detail = result['data'];
            }
            else {
                chooseGradeDiv.classList.add('d-none');
                chooseLessonDiv.classList.remove('d-none');
                contentError.classList.add('d-none');
                serverError.classList.remove('d-none');
            }
        }
    });

    if(detail.length == 0) {
        chooseGradeDiv.classList.add('d-none');
        chooseLessonDiv.classList.remove('d-none');
        contentError.classList.remove('d-none');
        serverError.classList.add('d-none');
        return;
    }

    lessonCard.innerHTML = '';
    for(let i = 0; i < detail.length; i++) {
        let section = '<div class="col-xl-6 col-lg-6 col-md-12 col-sm-12">'
        section += '<div class="release">'
        section += '<div class="release__content">'
        section += '<div class="release__cover">'
        // Image
        section += '<img src="/static/img/lessons/'
        section += detail[i]['image']
        section += '.jpg" alt="lesson image">'
        // Section number
        section += '</div>'
        section += '<div class="release__stat">'
        section += '<span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M17.211,3.39H2.788c-0.22,0-0.4,0.18-0.4,0.4v9.614c0,0.221,0.181,0.402,0.4,0.402h3.206v2.402c0,0.363,0.429,0.533,0.683,0.285l2.72-2.688h7.814c0.221,0,0.401-0.182,0.401-0.402V3.79C17.612,3.569,17.432,3.39,17.211,3.39M16.811,13.004H9.232c-0.106,0-0.206,0.043-0.282,0.117L6.795,15.25v-1.846c0-0.219-0.18-0.4-0.401-0.4H3.189V4.19h13.622V13.004z"/></svg>'
        section += detail[i]['sections_num']
        section += ' فصل</span>'
        section += '</div>'
        section += '</div>'
        // Sections
        section += '<div class="release__list">'
        section += ''
        section += '<ul class="main__list main__list--playlist main__list--dashbox">'

        for(let j = 0; j < detail[i]['sections_num']; j++) {
            section += '<li class="single-item">'
            section += '<div class="single-item__title">'
            section += '<h4><a class="lesson-session" href="#">فصل '
            section += (j+1).toString()
            section += '</a></h4>'
            section += '<small class="text-white">'
            section += detail[i]['sections_intro'][j+1]
            section += '</small>'
            section += '</div>'
            section += '</li>'

        }
        section += '</ul>'
        section += '</div>'
        section += '</div>'
        section += '</div>'

        content.push(section)
    }

    for(let i = 0; i < content.length; i++) {
        lessonCard.innerHTML += content[i]
    }

    chooseGradeDiv.classList.add('d-none');
    chooseLessonDiv.classList.remove('d-none');

    // Lesson card scroll (get from main.js line 333)
    if ($('.release__list').length) {
		let releaseLists = document.querySelectorAll('.release__list');
		for(let j = 0; j < releaseLists.length; j++) {
			Scrollbar.init(releaseLists[j], {
				damping: 0.1,
				renderByPixels: true,
				alwaysShowTracks: true,
				continuousScrolling: true
			});
		}

	}

    let sessions = document.querySelectorAll('.lesson-session');
    for(let i = 0; i < sessions.length; i++) {
        sessions[i].addEventListener('click', chooseSession)
    }
}

function chooseSession(e) {
    let selectedSession = e.target;
    let theSession = selectedSession.innerHTML;
    let lessonCard = selectedSession.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
    let lessonImage = lessonCard.querySelector('img').src.split("/").pop().split(".")[0];
    if(lessonImage.includes('Riazi')) {
        userLesson = 1;
    }
    else if(lessonImage.includes('Oloom')) {
        userLesson = 2;
    }

    let match = theSession.match(/\d+/); 
    let userSession = match ? parseInt(match[0]) : null; 

    let pigeon = {
        grade: userGrade,
        lesson: userLesson,
        session: userSession
    }

    console.log(userGrade, userLesson, userSession)
    $.ajax({
        type: "POST",
        url: "/game",
        async: false,
        data: JSON.stringify(pigeon),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(result) {
            console.log(result)
            let distination = 'http://' + window.location.host + '/game';
            window.location.replace(distination)
        }
    });
}

// function helpMe() {
//     let islandId = document.querySelector('#island-id').value;
//     let groupId = document.querySelector('#group-id').value;
//     let level = document.querySelector('#level-id').innerHTML;
//     let pigeon = {
//         island_id: islandId,
//         level: level,
//         group_id: groupId
//     }

//     console.log(pigeon)

//     $.ajax({
//         type: "POST",
//         url: "/req-help",
//         data: JSON.stringify(pigeon),
//         contentType: "application/json; charset=utf-8",
//         dataType: "json",
//         success: function(result) {
//             if(result['status'] == 'done') {
//                 location.reload();
//             }
//             else if(result['status'] == 'low') {
//                 // noChoose.classList.add('d-none');
//                 // lowBudget.classList.remove('d-none');
//             }
//         }
//       });
// }

// function removeHelp(e) {
//     let selectedHelp = e.target;
//     let helpDiv = selectedHelp.parentElement;
//     let helpId = helpDiv.querySelector('.help-id').value;
//     let pigeon = {
//         help_id: helpId
//     }
//     $.ajax({
//         type: "POST",
//         url: "/remove-help",
//         data: JSON.stringify(pigeon),
//         contentType: "application/json; charset=utf-8",
//         dataType: "json",
//         success: function(result) {
//             if(result['status'] == 'done') {
//                 location.reload();
//             }
//             else if(result['status'] == 'low') {
//                 // noChoose.classList.add('d-none');
//                 // lowBudget.classList.remove('d-none');
//             }
//         }
//       });
// }
