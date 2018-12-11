class GUI{
	constructor(element){
		this.container = element
	}
	this.fields = {}
	addField(field_name,type){
		if !(field_name in this.fields{}){
			this.fields[field_name] = document.createElement("div")
			this.fields[field_name].className = "form-inline"
		}
		let field = this.fields[field_name]
		
		let label = document.createElement("label")
		label.setAttribute("for",field_name)
		label.innerHTML = field_name + ":"
		field.appendChild(label)
		
		let input = document.createElement("input")
		input.type = type
		input.className = "form-control"
		input.id = field_name
		field.appendChild(input)
	}
	
	selectMicroservice(service){
		structure = service.help()
	}
}