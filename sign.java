Ankush Nmamit, [05-07-2022 10:26 PM]
package fxsignup;
import javafx.application.*;
import javafx.scene.*;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.event.*;
import javafx.stage.*;
//import javafx.geometry.*;

public class signup extends Application {
  Label user;
  public static void main(String[] args) {
    launch(args);
  }
  public void start(Stage myStage) {
    GridPane root=new GridPane();
    Button sign=new Button("Signup");
    TextField tf=new TextField();
    PasswordField pf=new PasswordField();
    user=new Label("Please Login");
    tf.setPromptText("Enter username");
    pf.setPromptText("Enter Password");
    sign.setOnAction(new EventHandler<ActionEvent>(){
      public void handle(ActionEvent ae) {
        user.setText("welcome " + tf.getText());
      }
    });
    root.add(tf, 1, 0);
    root.add(pf, 1, 2);
    root.add(sign, 1, 6);
    root.add(user, 1, 8);
    myStage.setTitle("User Login");
    myStage.setScene(new Scene(root,600,300));
    myStage.show();
  }

}
