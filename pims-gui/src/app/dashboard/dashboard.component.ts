import { Component, OnInit } from '@angular/core';
import { Color, LegendPosition, ScaleType } from '@swimlane/ngx-charts';
import { Subscription } from 'rxjs';
import { IPopulationDeathRatio } from '../interfaces/ipopulation-death-ratio';
import { PopulationDeathRatioService } from '../services/population-death-ratio.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  ratio: any[] = [];
  view: [number,number] = [300,200];

  //options
  gradient: boolean = true;
  showLegend: boolean = true;
  showLabels: boolean = false;
  isDoughnut: boolean = false;
  legendPosition: LegendPosition = LegendPosition.Below;

  colorScheme: Color = {
    domain: ['#5AA454', '#A10A28'],
    name: 'myScheme',
    selectable: false,
    group: ScaleType.Linear
  };

  constructor(private populationDeathRatio: PopulationDeathRatioService) { 
  }

  dra_sub!: Subscription;

  deathRatio!: IPopulationDeathRatio[];
  errorMessage: string = "";

  ngOnInit(): void {
    this.dra_sub = this.populationDeathRatio.getDeathRatio().subscribe({
      next: dras => this.deathRatio = dras,
      error: err => this.errorMessage = err
    })
  }

  onSelect(data): void {
    console.log('Item clicked', JSON.parse(JSON.stringify(data)));
  }

  onActivate(data): void {
    console.log('Activate', JSON.parse(JSON.stringify(data)));
  }

  onDeactivate(data): void {
    console.log('Deactivate', JSON.parse(JSON.stringify(data)));
  }

}
