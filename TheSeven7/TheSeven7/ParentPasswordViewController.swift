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
   
    var password = ""
    //var password = UserDefaults.standard.string(forKey: "parentPassword")
    
    override func viewDidLoad() {
        super.viewDidLoad()
        passwordTextField.delegate = self
        self.passwordTextField.autocapitalizationType = .allCharacters
        passwordTextField.addTarget(self, action: #selector(ParentPasswordViewController.textFieldDidChange(_:)), for: UIControl.Event.editingChanged)
        
        let localHost = UserDefaults.standard.string(forKey: "localhost")
        let url = URL(string: localHost! + "/parentpassword")!
        let task = URLSession.shared.dataTask(with: url) {(data, response, error) in
            guard let data = data else {
                return
            }
            self.password = self.convertToDictionary(text: String(data: data, encoding: .utf8)!)!["password"] as! String
            //print(self.convertToDictionary(text: String(data: data, encoding: .utf8)!)!["password"])
        }
        task.resume()
    }
    
    func convertToDictionary(text: String) -> [String: Any]? {
        if let data = text.data(using: .utf8) {
            do {
                return try JSONSerialization.jsonObject(with: data, options: []) as? [String: Any]
            } catch {
                print(error.localizedDescription)
            }
        }
        return nil
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
