import { Component, OnInit, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { DeathRates, MaritalCounts, AverageSalary, PositionSalary } from './data';

@Component({
  selector: 'app-graphs',
  templateUrl: './graphs.component.html',
  styleUrls: ['./graphs.component.css']
})
export class GraphsComponent implements OnInit {
  DeathRates!: any[];
  MaritalCounts!: any[];
  AverageSalary!: any[];
  PositionSalary!: any[];
  
  
  showXAxis = true;
  showYAxis = true;
  gradient = false;
  showLegend = false;
  showXAxisLabel = true;
  showYAxisLabel = true;
  timeline: boolean = true;
  
  
  Graph1X = 'State';
  Graph1Y = 'Death Rate';
  
  Graph2X = 'State';
  Graph2Y = 'Marital Counts';
  
  Graph3X = 'Company';
  Graph3Y = 'Average Salary';
  
  Graph4X = 'Company';
  Graph4Y = 'Salary';
  
  constructor() { 
    Object.assign(this, { DeathRates, MaritalCounts, AverageSalary, PositionSalary })
  }

  ngOnInit(): void {
  }

}
