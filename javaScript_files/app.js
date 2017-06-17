
$('#SignUpButton').on('click', function(){
	console.log('ya se dio cuenta que quiero hacer sign up')
	var first_name = $('#first_name').val()
	var last_name = $('#last_name').val()
	var client = $('#client').val()
	var email = $('#email').val()
	var confirm_email = $('#confirm_email').val()
	var password = $('#password').val()
	$('#success_message').addClass('hidden');

	$.ajax({
		type: "POST",
		url: "/CrearUsuario",
		dataType: 'json',
		data: JSON.stringify({
			'user_action': 'SignUp',
			'first_name': first_name,
			'last_name':last_name,
			'email':email,
			'confirm_email':confirm_email,
			'is_administrator':$('#is_administrator').is(':checked'),
			'password':password,
			'client': client,		
		})
	})
	.done(function(data){
		var next_step = data['next_step'];
		console.log(next_step);


		if (next_step == 'TryAgain'){
			$('#input_error').text(data['input_error'])							
		};

		if (next_step == 'UserCreated'){
			$('#input_error').text('');
			$('#success_message').removeClass('hidden');
			$('#first_name').val('')
			$('#last_name').val('')
			$('#email').val('')
			$('#confirm_email').val('')
			$('#password').val('')
			$('#client').val('')
			$('#is_administrator').prop('checked', false)
		};
	})		
});


$('#LogInButton').on('click', function(){
	console.log('Si se dio cuenta de que quiero hacer login')

	var email = $('#login_email').val();
	var password = $('#login_password').val();

	$.ajax({
		type: "POST",
		url: "/LogIn",
		dataType: 'json',
		data: JSON.stringify({
			'user_action': 'LogIn',
			'email':email,
			'password':password		
		})
	})
	.done(function(data){
		var next_step = data['next_step'];
		console.log(next_step);

		if (next_step == 'SuccesfulLogIn'){
			window.location.href = '/VisualizadorCNBV'
		};

		if (next_step == 'TryAgain'){
			$('#InvalidEmailOrPasswordError').removeClass('hidden');			
			
		};
	})		
});


$('#RequestPasswordReset').on('click', function(){
	var user_email = $('#user_email').val()
	$.ajax({
		type: "POST",
		url: "/Accounts",
		dataType: 'json',
		data: JSON.stringify({
			'user_action': 'RequestPasswordReset',
			'user_email': user_email,			
		})
	})
	.done(function(data){
		var next_step = data['next_step'];
		console.log(next_step);

		if (next_step == 'EnterValidEmail'){
			$('#InvalidEmailError').removeClass('hidden');
		};

		if (next_step == 'CheckYourEmail'){
			$('#request_reset_email').toggleClass('hidden');
			$('#reset_email_sent').toggleClass('hidden');
		};
	})		
});


$('#PasswordResetButton').on('click', function(){
	var usuario_id = $('#usuario_id').val()
	var password_hash = $('#password_hash').val()
	var new_password = $('#NewPassword').val()
	$.ajax({
		type: "POST",
		url: "/Accounts",
		dataType: 'json',
		data: JSON.stringify({
			'user_action': 'SetNewPassword',
			'new_password': new_password,
			'usuario_id':usuario_id,
			'password_hash':password_hash		
		})
	})
	.done(function(data){
		var next_step = data['next_step'];
		console.log(next_step);

		if (next_step == 'EnterValidPassword'){
			$('#InvalidPasswordError').removeClass('hidden');
		};

		if (next_step == 'GoToLandingPage'){
			$('#enter_new_password').toggleClass('hidden');
			$('#password_reseted').toggleClass('hidden');
			
		};
	})		
});


function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}

$("#imgInp").change(function(){
    readURL(this);
});

$(document).on('focusin', '.QuickAttributeUpdate', function(){
	
	var attr_value = $(this).val();

	$(this).on('focusout', function(){
		if(attr_value != $(this).val()){
			
			var attr_key = $(this).attr("name");
			var attr_value = $(this).val();
			if($(this).attr("type") == 'checkbox'){
				attr_value = $(this).is(':checked');
			}; 
			
			var target = $(this).closest('#DeckEditorSlide');
			var target_type = 'slide'

			console.log(target)
			if(target.attr("value") == undefined){
				target = $(this).closest('#UserEditorUser');
				target_type = 'user' 	
			};
			console.log(target_type)

			var target_id = target.attr("value");

			console.log(attr_key);
			console.log(attr_value);
			
			if (target_type == 'slide'){
				$.ajax({
					type: "POST",
					url: "/DeckEditor",
					dataType: 'json',
					data: JSON.stringify({
						'slide_id': target_id,
						'user_action': 'UpdateSlide',
						'attr_key':attr_key,
						'attr_value':attr_value,
					})
				}).done(function(data){console.log(data['message'])})

			}

			if (target_type == 'user'){
				$.ajax({
					type: "POST",
					url: "/UserEditor",
					dataType: 'json',
					data: JSON.stringify({
						'user_id': target_id,
						'user_action': 'UpdateUser',
						'attr_key':attr_key,
						'attr_value':attr_value,
					})
				}).done(function(data){console.log(data['message'])})

			}


		}
	})
});


$(document).on('click', '.DeleteButton', function(){
	
	var target = $(this).closest('#DeckEditorSlide');
	var target_type = 'slide'

	if(target.attr("value") == undefined){
		target = $(this).closest('#UserEditorUser');
		target_type = 'user' 	
	};
	console.log(target_type)

	var target_id = target.attr("value");

	target.fadeOut("slow")

	if(target_type == 'slide'){
		$.ajax({
			type: "POST",
			url: "/DeckEditor",
			dataType: 'json',
			data: JSON.stringify({
				'slide_id': target_id,
				'user_action': 'DeleteSlide'
			})
		}).done(function(data){
			console.log(data['message']);
			target.addClass('hidden');
			})
	}

	if(target_type == 'user'){
		$.ajax({
			type: "POST",
			url: "/UserEditor",
			dataType: 'json',
			data: JSON.stringify({
				'user_id': target_id,
				'user_action': 'DeleteUser'
			})
		}).done(function(data){
			console.log(data['message']);
			target.addClass('hidden');
			})
	}


});


var past_slide = 0;
var current_slide = 0;
var next_slide = 0;


function UpdateCurrentNextPreviews(movement){
	var SeccionActiva = $('.SeccionActiva');
	var TamanoSeccion = SeccionActiva.length;
	
	if(movement == 'right'){
		past_slide = current_slide
		current_slide = next_slide
		
		if(next_slide + 1 < TamanoSeccion ){
			next_slide = next_slide + 1
		}
	}

	if(movement == 'left'){
		next_slide = current_slide
		current_slide = past_slide
				
		if(past_slide - 1 >= 0 ){
			past_slide = past_slide - 1
		}
	}
};

$(document).on('click', '.SectionButton', function(){
	$('.ReportSlide').addClass('hidden')
	$('.ReportSlide').removeClass('SeccionActiva')
	var seccion_objetivo = $(this).attr('seccion_objetivo');
	console.log(seccion_objetivo);
	// $(seccion_objetivo).removeClass('hidden')
	$(seccion_objetivo).addClass('SeccionActiva');
	$($(seccion_objetivo)[0]).removeClass('hidden');

	past_slide = 0;
	current_slide = 0;
	next_slide = 1;
});



$('.MovementButton').on('click', function(){
	var movement = $(this).attr('movement');
	var SeccionActiva = $('.SeccionActiva');
	$(SeccionActiva[current_slide]).addClass('hidden');

	if(movement == 'right'){	
		$(SeccionActiva[next_slide]).removeClass('hidden');		
	}

	if(movement == 'left'){
		$(SeccionActiva[past_slide]).removeClass('hidden');	
	}
	UpdateCurrentNextPreviews(movement)

});

$(document).on('click', '.DeleteTableButton', function(){
	
	var table = $(this).closest('#TableViewerTable');
	var table_name = $(this).attr("table_name")
	var table_id = table.attr("value");
	// table.fadeOut("slow")
	
	console.log('This is the table to be deleted:')
	console.log(table_name)

	$.ajax({
		type: "POST",
		url: "/TableViewer",
		dataType: 'json',
		data: JSON.stringify({
			'table_name': table_name,
			'table_id': table_id,
			'user_action': 'DeleteTable'
		})
	}).done(function(data){
		console.log(data['message']);
		console.log(data['RowsDeleted']);
		console.log(data['RowsLeft'])
		// table.addClass('hidden');
		})
});