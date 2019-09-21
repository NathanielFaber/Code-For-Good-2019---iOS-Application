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
   
    let password = UserDefaults.standard.string(forKey: "parentPassword")
    
    override func viewDidLoad() {
        super.viewDidLoad()
        passwordTextField.delegate = self
        self.passwordTextField.autocapitalizationType = .allCharacters
        passwordTextField.addTarget(self, action: #selector(ParentPasswordViewController.textFieldDidChange(_:)), for: UIControl.Event.editingChanged)
    }
    
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        
        let currentCharacterCount = textField.text?.count ?? 0
        if range.length + range.location > currentCharacterCount {
            return false
        }
        let newLength = currentCharacterCount + string.count - range.length
        return newLength <= 4
    }
    
    @objc func textFieldDidChange(_ textField: UITextField) {
        if (passwordTextField.text == password) {
            performSegue(withIdentifier: "password", sender: self)
            passwordTextField.resignFirstResponder()
        }
    }
}
