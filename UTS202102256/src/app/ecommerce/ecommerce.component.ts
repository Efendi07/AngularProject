import { Component, OnInit, Renderer2 } from '@angular/core';

@Component({
  selector: 'app-ecommerce',
  templateUrl: './ecommerce.component.html',
  styleUrls: ['./ecommerce.component.css']
})
export class EcommerceComponent implements OnInit {

  constructor(private renderer : Renderer2) {
    this.renderer.addClass(document.body, "content-page");
   }

  ngOnInit(): void {
  }

}
