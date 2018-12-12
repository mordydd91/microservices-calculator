class GUI{
	constructor(body,title,fields={}){
		this.title = title
		this.container = document.createElement("div")
		let titleHeader = document.createElement("h2")
		titleHeader.innerHtml = title
		this.form = document.createElement("form")
		this.form.id = "form_" + this.title;
	}
	
	addField(field_name,type,form = this.form){
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
		
		form.appendChild(field)
	}
	
	addSubmit(text = "Submit"){
		if(this.button) {return}
		this.button = document.createElement("button")
		this.button.type = "submit"
		this.button.className = "btn btn-default"
		this.button.innerHTML = text
		this.container.appendChild(this.button)
	}
	
	selectMicroservice(service){
		structure = service.help()
	}
}

<div class="jumbotron text-center">
  <h2>Calculator Microservices</h2>
  <form id="form">
    <div class="form-inline">
      <label for="parameter 1">Parameter 1:</label>
      <input type="text" class="form-control" id="parameter 1" placeholder="1">
    </div>
    <div class="form-inline">
      <label for="parameter 2">Parameter 2:</label>
      <input type="text" class="form-control" id="parameter 2" placeholder="2">
    </div>
    <button type="submit" class="btn btn-default">Submit</button>
  </form>
</div>