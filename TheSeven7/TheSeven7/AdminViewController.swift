//
//  AdminViewController.swift
//  TheSeven7
//
//  Created by Nick Pappas on 9/20/19.
//  Copyright © 2019 Ayline Villegas . All rights reserved.
//

import UIKit

class AdminViewController: UIViewController, UITextFieldDelegate {

    @IBOutlet weak var parentPasswordTextField: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        parentPasswordTextField.delegate = self
        self.parentPasswordTextField.autocapitalizationType = .allCharacters
        if let password = UserDefaults.standard.string(forKey: "parentPassword") {
            parentPasswordTextField.placeholder = password
        }
        // Do any additional setup after loading the view.
    }
    
    @IBAction func setButtonPress(_ sender: Any) {
        let defaults = UserDefaults.standard
        defaults.set(parentPasswordTextField.text, forKey: "parentPassword")
        parentPasswordTextField.placeholder = parentPasswordTextField.text
    }
    
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        
        let currentCharacterCount = textField.text?.count ?? 0
        if range.length + range.location > currentCharacterCount {
            return false
        }
        let newLength = currentCharacterCount + string.count - range.length
        return newLength <= 4
    }
}
