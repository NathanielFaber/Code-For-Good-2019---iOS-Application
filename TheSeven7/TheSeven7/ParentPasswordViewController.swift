//
//  ParentPasswordViewController.swift
//  TheSeven7
//
//  Created by Nick Pappas on 9/20/19.
//  Copyright © 2019 Ayline Villegas . All rights reserved.
//

import UIKit
import TextFieldEffects

class ParentPasswordViewController: UIViewController, UITextFieldDelegate {

    @IBOutlet weak var passwordTextField: HoshiTextField!
   
    override func viewDidLoad() {
        super.viewDidLoad()
        passwordTextField.delegate = self
        self.passwordTextField.autocapitalizationType = .allCharacters
    }
    
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        
        let currentCharacterCount = textField.text?.count ?? 0
        if range.length + range.location > currentCharacterCount {
            return false
        }
        let newLength = currentCharacterCount + string.count - range.length
        return newLength <= 4
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
