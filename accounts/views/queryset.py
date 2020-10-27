    queryset=model.objects.get(is_staff=True).order_by('username')
    def get_context_data():

    <input type="text" class="form-control" id="Nombreusuario" placeholder="Usuario" value="{{ user.username }}">