{% extends 'main/header.html'%}

{% block title %}
Регистрация
{% endblock %}

{% block body %}
<?php
require('connect.php');

if(isset($_POST['email']) && isset($_POST['password'])){
    $email = $_POST['email'];
    $password = $_POST['password'];
    if(filter_var($email, FILTER_VALIDATE_EMAIL)){
        $query = "INSERT INTO wtdb.users (email, password) VALUES('$email', '$password')";
        $result = mysqli_query($connection, $query);
        if($result){
            $smsg = "Регистрация прошла учпешно";
        } else{
            $fsmsg = "Ошибка";
        }
    } else{
        $uncur_email = "Почта указана неверно";
    }
}
?>
    <div class="container">
        <form class="form-signin" method="POST">
            <h2>Регистрация</h2>
            <?php if(isset($smsg)){ ?><div class="alert alert-success" role="alert">
                <?php echo $smsg; sleep(5); header("Location: ./succesreg.php");
                ?></div><?php }?>
            <?php if(isset($fsmsg)){ ?><div class="alert alert-danger" role="alert"> <?php echo $fsmsg; ?>
                </div><?php }?>
            <?php if(isset($uncur_email)){ ?><div class="alert alert-danger" role="alert"> <?php echo $uncur_email; ?>
                </div><?php }?>

            <input type="text" name="email" class="form-control" placeholder="Email" required>
            <input type="password" name="password" class="form-control" placeholder="Пароль" required>
            <button class="btn btn-lg btn-primary btn-block" type="submit">Зарегистрироваться</button>
        </form>
    </div>

<?php
if(isset($_SESSION['email'])){
        $tmp = $_SESSION['email'];
        echo "hello $tmp";
    } else{
    echo "NNNNNN";
}
?>
{% endblock %}

