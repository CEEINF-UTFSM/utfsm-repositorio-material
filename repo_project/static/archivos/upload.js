let select_carrera = document.querySelector("#select-carrera")
let select_semestre =  document.querySelector("#select-semestre")
let select_ramo =  document.querySelector("#select-ramo")

let carrera_ramos = []
select_carrera.addEventListener('change', function (e) { 
	let carrera = select_carrera.value
	carrera = carreras.find(e => e.pk == carrera)
	semestres = 0

	carrera_ramos = []
	for (ramo of carrera.fields.ramos){
		let r = ramos.find(e => e.pk == ramo)
		console.log(r)

		carrera_ramos.push(r)

		if (semestres < r.fields.semestre) semestres = r.fields.semestre
		
	}
	select_semestre.textContent = '';
	select_ramo.textContent = '';

	option = document.createElement("option")
	option.textContent = 'Semestre'
	option.disabled = option.selected = true
	select_semestre.appendChild(option)
	for (i = 1; i <= semestres; i++){
		option = document.createElement("option")
		option.value = option.textContent = i
		select_semestre.appendChild(option)
	}
	select_semestre.disabled = false

})
select_semestre.addEventListener('change', function (e) { 
	let carrera = select_carrera.value
	let semestre = select_semestre.value
	carrera = carreras.find(e => e.pk == carrera)

	select_ramo.textContent = '';

	option = document.createElement("option")
	option.textContent = 'Ramo'
	option.disabled = option.selected = true
	select_ramo.appendChild(option)

	semestre_ramos = carrera_ramos.filter(e => e.fields.semestre == semestre)
	for (r of semestre_ramos){
		option = document.createElement("option")
		option.value = r.pk;
		option.textContent = r.fields.nombre
		select_ramo.appendChild(option)

		
		console.log(r)
	}

	select_ramo.disabled = false

})