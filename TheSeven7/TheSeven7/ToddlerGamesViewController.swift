//
//  ToddlerGamesViewController.swift
//  TheSeven7
//
//  Created by Nick Pappas on 9/21/19.
//  Copyright © 2019 Ayline Villegas . All rights reserved.
//

import UIKit

class ToddlerGamesViewController: UIViewController {

    var urlString = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    @IBOutlet weak var aa: UIView!
    @IBAction func trainGame(_ sender: Any) {
        urlString = "https://www.happyclicks.net/touch-tap-games/baby_games_train.php"
        performSegue(withIdentifier: "gameSegue", sender: self)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?)
    {
        if segue.destination is GamesViewController
        {
            let vc = segue.destination as? GamesViewController
            vc?.urlString = urlString
        }
    }
}
