import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SelectReferenceFaceComponent } from './select-reference-face.component';

describe('SelectReferenceFaceComponent', () => {
  let component: SelectReferenceFaceComponent;
  let fixture: ComponentFixture<SelectReferenceFaceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SelectReferenceFaceComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SelectReferenceFaceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
