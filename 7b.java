Ankush Nmamit, [05-07-2022 10:26 PM]
package javafxdemo;
import javafx.application.*;
import javafx.scene.*;
import javafx.stage.*;
import javafx.scene.layout.*;
import javafx.scene.control.*;
import javafx.event.*;
import javafx.geometry.*;
public class fxskeleton extends Application {
  Label response;
  public static void main(String[] args) {
    launch(args);
  }
  public void start(Stage myStage) {
    myStage.setTitle("Demonstrate buttons");
    GridPane root=new GridPane();
//    FlowPane root=new FlowPane(10,10);
//    root.setAlignment(Pos.CENTER);
    response = new Label("Push a button");
    Button alpha=new Button("Alpha");
    Button beta=new Button("Beta");
    alpha.setOnAction(new EventHandler<ActionEvent>() {
      public void handle(ActionEvent ae) {
        response.setText("Alpha was pressed");
      }
    });
    beta.setOnAction(new EventHandler<ActionEvent>() {
      public void handle(ActionEvent ae) {
        response.setText("Beta was pressed");
      }
    });
    root.add(response, 1, 0);
    root.add(beta, 2,1);
    root.add(alpha, 0, 1);
    myStage.setScene(new Scene(root,600,200));
//    root.getChildren().addAll(alpha,beta,response);
    myStage.show();
    
  }
}
